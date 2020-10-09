from haystack import indexes

from .models import Movie


class MovieIndex(indexes.SearchIndex, indexes.Indexable):
    name = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='user')
    pub_date = indexes.DateTimeField(model_attr='pub_date')

    def get_model(self):
        return Note

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(
            pub_date__lte=datetime.datetime.now()
        )
