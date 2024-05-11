from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("""
    <h1>Hola Mundo!</h1>
    """)

def about(request):
    return HttpResponse("""
    <h3>What is Lorem Ipsum?</h3>
                        
    <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.</p>
    """)

def contact(request):
    return HttpResponse("""
    <form action="/my-handling-form-page" method="post">
    <ul>
        <li>
            <label for="name">Nombre:</label>
            <input type="text" id="name" name="user_name" />
        </li>
        <li>
            <label for="mail">Correo electrónico:</label>
            <input type="email" id="mail" name="user_mail" />
        </li>
        <li>
            <label for="msg">Mensaje:</label>
            <textarea id="msg" name="user_message"></textarea>
        </li>
    </ul>
    </form>
    """)