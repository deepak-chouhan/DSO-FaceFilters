from django.shortcuts import render
from django.http import StreamingHttpResponse, JsonResponse
from . import videoCamera

cam = videoCamera.VideoCamera()

def index(request):
    return render(request, "CaptureData/index.html")

def setFilter(request):
    filter_name = request.GET.get('filter-name')
    current_filter = cam.setFilter(str(filter_name))
    return JsonResponse({'success': True,
                         "current-filter": current_filter})

def sendVideo(request):
    try:
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except Exception as e:
        print(f"Exception Occured: {e}")
        return JsonResponse({
            "success": False,
            "error": str(e)
        })

def gen(camera):
    while True:
        try:
            frame = camera.getFrame()
            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        except Exception as e:
            print(f"Exception occurred while generating frame: {e}")
            break