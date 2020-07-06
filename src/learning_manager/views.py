from .models import Person
from django.views import generic


def update_context_data(context, editors, persons):
    # Get the blog from id and add it to the context
    context['show_link_editors'] = editors
    context['show_link_authors'] = persons
    return context


class IndexPersonsView(generic.ListView):
    def get_queryset(self):
        return Person.peoples.all()[:5]

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(IndexPersonsView, self).get_context_data(**kwargs)
        return update_context_data(context, True, True)


class IndexEditorView(generic.ListView):
    def get_queryset(self):
        return Person.peoples.editors()[:5]

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(IndexEditorView, self).get_context_data(**kwargs)
        return update_context_data(context, False, True)


class IndexAuthorView(generic.ListView):
    def get_queryset(self):
        return Person.peoples.authors()[:5]

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(IndexAuthorView, self).get_context_data(**kwargs)
        return update_context_data(context, True, False)


class DetailPersonView(generic.DetailView):
    def get_queryset(self):
        return Person.peoples
