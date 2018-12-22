from django.db import models


class DocFile(models.Model):
    contract_Title = models.CharField(max_length=50)
    contract_Doc_File = models.FileField(upload_to='uploads')

    def __str__(self):
        return self.contract_Title

    def delete(self, *args, **kwargs):
        self.contract_Doc_File.delete()
        super().delete(*args, **kwargs)
