from http.client import HTTPResponse
from django.http import (
    HttpRequest,
    HttpResponse,
)
from django.shortcuts import (
    render,
    get_object_or_404,
)

from .models import Section
from .forms import ApplicationForm


def index(request: HttpRequest) -> HTTPResponse:
    """Обработчик главной страницы"""

    context = {
        'sections': Section.objects.all(),
    }

    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            context['errors'] = form.errors

    return render(
        request=request,
        template_name='main_app/index.html',
        context=context,
    )

def section(request: HttpRequest, section_id: int) -> HttpResponse:
    """Обработчик страницы раздела с услугами"""

    current_section = get_object_or_404(Section, pk=section_id)

    context = {
        'section': current_section,
    }

    return render(
        request=request,
        template_name='main_app/section.html',
        context=context,
    )
