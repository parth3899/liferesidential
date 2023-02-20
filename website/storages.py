from django.conf import settings
from django.core.files.storage import get_storage_class

from storages.backends.s3boto3 import S3Boto3Storage


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION


class CachedS3BotoStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.local_storage = get_storage_class(
            'compressor.storage.CompressorFileStorage'
        )()

    def save(self, name, content):
        self.local_storage._save(name, content)
        super().save(name, self.local_storage._open(name))
        return name
