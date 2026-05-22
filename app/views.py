from django.shortcuts import render

def home_main(request):
    return render(request, 'home/home_main.html')

def space_main(request):
    return render(request, 'space/space_main.html')

def memory_main(request):
    return render(request, 'memory/memory_main.html')

def mypage_main(request):
    return render(request, 'mypage/mypage_main.html')

def onboarding(request):
    return render(request, 'onboarding/onboarding.html')

def home_create_room1(request):
    return render(request, 'home/home_create_room1.html')

def home_create_room2(request):
    return render(request, 'home/home_create_room2.html')

def home_join_room(request):
    return render(request, 'home/home_join_room.html')