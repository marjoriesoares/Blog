# Final Project - Python Course - Coderhouse

## Blog Project – Python Framework Django

The project is considered a MVT project due to the software design pattern for developing web applications Django is based on: MVT (Model-View-Template) architecture. 
To run this project, you will only have to have Python, Django and Pillow installed.
To install Django type in the terminal:
•	Pip install Django
To install Pillow type in the terminal:
• Pip install Pillow


The directories we will need are configured in settings.py to work without issues on your computer, since only relative paths were used.
The Blog has:

<li> A main page with brief information about the posts and URLs redirecting the user to the posts.</li>
<li> An about session with introduction to the author.</li>
<li> A profile session.</li>
<li> A message session.</li>

The Blog also has 2 complete cicles of CRUD (Create, Read, Update and Delete), one for accounts and one for pages.

1. Accounts

- In the navigation bar you can find two options related to accounts if you are not signed in: sign up and login.
![image](https://user-images.githubusercontent.com/108837573/193108229-c0b26bdc-5a96-4458-a5c3-0216fa6e50aa.png)
- In sign up you can register a new account. When this step is finished, the system will generate  automatically an empty profile related to that account that can be filled later in edit profile. 
![image](https://user-images.githubusercontent.com/108837573/193109315-6e8c7a11-2ada-46df-bc63-f8c3f583d38a.png)
- The user is redirected to the login page to start session.
![image](https://user-images.githubusercontent.com/108837573/193109604-a9644d28-7575-4622-99d8-a3b200f0b187.png)
- After the session starts, the user is redirected to the homepage and the navigation bar changes: the sign up and login options disappear and you are able to find the username to access the profile of the user.
![image](https://user-images.githubusercontent.com/108837573/193110186-b41039b7-85ef-4144-a7aa-3312ffbe406f.png)
- The profile of the user is generated with a default picture and has information from the register form and from the profile form that are still blank until the user edits it.
![image](https://user-images.githubusercontent.com/108837573/193110555-6576dd6d-5af0-435c-8b0f-2b6cda231252.png)
- The other options found in the profile page are: Edit Profile, Delete Account, and Sign Out.

2. Pages
- the main page has a list with an overview of all posts and the user can select one to read the entire post.
![image](https://user-images.githubusercontent.com/108837573/193111140-036c9d9b-d0cb-49ee-96a8-3ea191ff3b4a.png)
- The overview of the pages contains: Photo, Title, Subtitle, Author, Date and the first 200 caracters of the post.
- In the detailed view of the chosen page you will find options to edit the post, delete the post or create a new one.
![image](https://user-images.githubusercontent.com/108837573/193111610-db5a9911-fd35-4b71-996c-63f18b6edb3a.png)
- The pages can be created using an text editor.
![image](https://user-images.githubusercontent.com/108837573/193111810-5ac56b51-4abe-4ddc-853e-3abe552accfc.png)

3. Admin portal
- The admin portal contains the authorization module, that is a build in function of Django, and the two models: Pages and Accounts.
![image](https://user-images.githubusercontent.com/108837573/193112121-6ebf604b-b827-433a-8c34-67e00fd926e6.png)
- You can use the admin portal to create, edit or delete any of the instances.

4. Messages
- This part is still being worked on.
![image](https://user-images.githubusercontent.com/108837573/193112735-574d6753-0f53-4761-b7df-a3953a85ade2.png)

5. You can find the test cases and video showing the Blog functionality here:
https://drive.google.com/drive/folders/1LoqdnUcUxfRXERW48Hles702han5th12?usp=sharing

------------------------------------ Spanish Translation ------------------------------------ 

El proyecto se considera un proyecto MVT debido al patrón de diseño de software para el desarrollo de aplicaciones web en el que django se basa: arquitectura MVT (Model-View-Template). 
Para ejecutar este proyecto, solo tendrás que tener instalado Python, Django y Pillow.
Para instalar Django escriba en el terminal:
• Pip install Django
Para instalar Pillow  en el terminal:
• Pip install Pillow

Los directorios que necesitaremos están configurados en settings.py para que funcionen sin problemas en tu ordenador, ya que solo se utilizaron rutas relativas.
El Blog tiene:

<li> Una página principal con información breve sobre las publicaciones y URL que redirigen al usuario a las publicaciones.</li>
<li> Una sesión sobre con introducción al autor.</li>
<li> Una sesión de perfil.</li>
<li> Una sesión de mensajes.</li>

El Blog también cuenta con 2 ciclos completos de CRUD (Crear, Leer, Actualizar y Borrar), uno para cuentas y otro para páginas.

1. Cuentas

- En la barra de navegación puedes encontrar dos opciones relacionadas con las cuentas si no has iniciado sesión: registrarte e iniciar sesión.
- Al registrarse puede registrar una nueva cuenta. Cuando finalice este paso, el sistema generará automáticamente un perfil vacío relacionado con esa cuenta que se puede rellenar más adelante en el perfil de edición. 
- El usuario es redirigido a la página de inicio de sesión para iniciar la sesión.
- Después de que comienza la sesión, el usuario es redirigido a la página de inicio y la barra de navegación cambia: las opciones de registro e inicio de sesión desaparecen y puede encontrar el nombre de usuario para acceder al perfil del usuario.
- El perfil del usuario se genera con una imagen por defecto y tiene información del formulario de registro y del formulario de perfil que siguen en blanco hasta que el usuario lo edite.
- Las otras opciones que se encuentran en la página de perfil son: Editar perfil, Eliminar cuenta y Cerrar sesión.


2. Paginas
- la página principal tiene una lista con una visión general de todas las publicaciones y el usuario puede seleccionar una para leer la publicación completa.
- La descripción general de las páginas contiene: Foto, Título, Subtítulo, Autor, Fecha y los primeros 200 caracteres de la publicación.
- En la vista detallada de la página elegida encontrarás opciones para editar el post, eliminar el post o crear uno nuevo.
- Las páginas se pueden crear utilizando un editor de texto.

3. Portal de administración
- El portal de administración contiene el módulo de autorización, que es una función incorporada de Django, y los dos modelos: Páginas y Cuentas.
- Puede utilizar el portal de administración para crear, editar o eliminar cualquiera de las instancias.

4. Mensajes

Esta parte todavía se está trabajando.

5. Puede encontrar los casos de prueba y el video que muestra la funcionalidad del Blog aquí:
https://drive.google.com/drive/folders/1LoqdnUcUxfRXERW48Hles702han5th12?usp=sharing
