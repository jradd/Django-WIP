from django.shortcuts import get_object_or_404, render_to_response

from django.views.generic.dates import YearArchiveView, MonthArchiveView, DayArchiveView

from mysecuri.blog.models import Entry


class EntryYearArchiveView(YearArchiveView):
    queryset = Entry.objects.all()
    date_field = "pub_date"
    make_object_list = True
    allow_future = True

class EntryMonthArchiveView(MonthArchiveView):
    queryset = Entry.objects.all()
    date_field = "pub_date"
    make_objects_list = True
    allow_future = True

class EntryDayArchiveView(DayArchiveView):
    queryset = Entry.objects.all()
    date_field = "pub_date"
    make_objects_list = True
    allow_future = True

def entries_index(request):
    return render_to_response('blog/entry_index.html',
			      {'entry_list': Entry.objects.all()})
"""
def entry_detail(request, year, month, day, slug):
    import datetime, time
    date_stamp = time.strptime(year+month+day, "%Y%b%d")
    pub_date = datetime.date(*date_stamp[:3])
    entry = get_object_or_404(Entry,
			      pub_date__year=pub_date.year,
			      pub_date__month=pub_date.month,
			      pub_date__day=pub_date.day,
			      slug=slug)

    return render_to_response('blog/entry_detail.html',
			      {'entry': entry})
"""
