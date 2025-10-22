from django.http import HttpResponse

def whoamI(request):
    return HttpResponse(
        "<pre style='font-size:30px;line-height:2.0'>「台北商業大學\n五專資管科\n{11256008}\n{劉晉成}」</pre>",
        content_type="text/html; charset=utf-8",
    )