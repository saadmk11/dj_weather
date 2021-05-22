from django.contrib import messages
from django.views.generic import FormView

from weather.forms import LocationCoordinateForm
from weather.utils import get_weather_data


class WeatherView(FormView):
    template_name = 'weather/view_weather.html'
    form_class = LocationCoordinateForm

    def form_valid(self, form):
        lat = form.cleaned_data.get('latitude')
        lon = form.cleaned_data.get('longitude')

        success, data = get_weather_data(lat, lon)

        if success:
            extra_data = data
        else:
            messages.error(self.request, data['error'])
            extra_data = {}

        return self.render_to_response(
            self.get_context_data(
                form=form,
                weather_data=extra_data
            )
        )
