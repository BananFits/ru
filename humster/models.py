from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


# def translit_to_eng(s: str) -> str:
#     d = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
#          'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i', 'к': 'k',
#          'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
#          'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch',
#          'ш': 'sh', 'щ': 'shch', 'ь': '', 'ы': 'y', 'ъ': '', 'э': 'r', 'ю': 'yu', 'я': 'ya'}
#
#     return "".join(map(lambda x: d[x] if d.get(x, False) else x, s.lower()))

# Create your models here.
class Travel(models.Model):
    title = models.CharField(max_length=255, verbose_name='название')
    content = models.TextField(blank=True, verbose_name='подробно')
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    class Meta:
        verbose_name = "Путешествия"
        verbose_name_plural = "Путешествия"

    def get_absolute_url(self):
        return reverse('travelslug', kwargs={'sl': self.slug})
    # def save(self,*args,**kwargs):
    #     self.slug = slugify(translit_to_eng(self.title))
    #     super().save(*args,**kwargs)


