from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings


class MediaStorage(S3Boto3Storage):
    bucket_name = 'webpres'
    isfilecached = {}

    def isdir(self, name):
        if not name:  # Empty name is a directory
            return True

        if self.isfile(name):
            return False

        return True

    def isfile(self, name):
        if len(name.split('.')) > 1:
            return True
        try:
            name = self._normalize_name(self._clean_name(name))
            if self.isfilecached.get(name) is not None:
                return self.isfilecached.get(name)

            f = S3Boto3StorageFile(name, 'rb', self)
            if "directory" in f.obj.content_type:
                isfile = False
            else:
                isfile = True
        except Exception:
            isfile = False
        self.isfilecached[name] = isfile
        return isfile

    def move(self, old_file_name, new_file_name, allow_overwrite=False):

        if self.exists(new_file_name):
            if allow_overwrite:
                self.delete(new_file_name)
            else:
                raise "The destination file '%s' exists and allow_overwrite is False" % new_file_name

        old_key_name = self._encode_name(self._normalize_name(self._clean_name(old_file_name)))
        new_key_name = self._encode_name(self._normalize_name(self._clean_name(new_file_name)))

        k = self.bucket.meta.client.copy(
            {
                'Bucket': self.bucket.name,
                'Key': new_key_name
            },
            self.bucket.name,
            old_key_name
        )

        if not k:
            raise "Couldn't copy '%s' to '%s'" % (old_file_name, new_file_name)

        self.delete(old_file_name)

    def makedirs(self, name):
        name = self._normalize_name(self._clean_name(name))
        return self.bucket.meta.client.put_object(Bucket=self.bucket.name, Key=f'{name}/')

    def rmtree(self, name):
        name = self._normalize_name(self._clean_name(name))
        delete_objects = [{'Key': f"{name}/"}]

        dirlist = self.listdir(self._encode_name(name))
        for item in dirlist:
            for obj in item:
                obj_name = f"{name}/{obj}"
                if self.isdir(obj_name):
                    obj_name = f"{obj_name}/"
                delete_objects.append({'Key': obj_name})
        self.bucket.delete_objects(Delete={'Objects': delete_objects})

    def path(self, name):
        return name

    def listdir(self, name):
        directories, files = super().listdir(name)
        if '.' in files:
            files.remove('.')
        return directories, files

    def exists(self, name):
        if self.isdir(name):
            return True
        else:
            return super().exists(name)

    def get_modified_time(self, name):
        try:
            # S3 boto3 library requires that directorys have the trailing slash
            if self.isdir(name):
                name = f'{name}/'
            modified_date = super().get_modified_time(name)
        except Exception:
            modified_date = timezone.now()
        return modified_date

    def size(self, name):
        try:
            # S3 boto3 library requires that directorys have the trailing slash
            if self.isdir(name):
                name = f'{name}/'
            size = super().size(name)
        except Exception:
            size = 0
        return size

