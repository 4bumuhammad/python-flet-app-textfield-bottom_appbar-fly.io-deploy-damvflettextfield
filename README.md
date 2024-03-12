# Python : flet app textfield bottom_appbar fly.io deploy damvflettextfield


files structure :

    ❯ tree -L 2 -I 'gambar-petunjuk|README.md'

        ├── Dockerfile
        ├── main.py
        └── requirements.txt

#### code :

- python

    ❯ vim main.py


        import flet as ft

        def main(page: ft.Page):
            page.title = "DAMv Test" 

            page.appbar = ft.AppBar(
                title=ft.Text("Flet Test Home Page", color=ft.colors.WHITE),  
                bgcolor=ft.colors.BLUE,  
                center_title=True  
            )

            text_field_name = ft.TextField(value="", 
                                    label="Name",
                                    hint_text="Enter text here", 
                                    text_size=50,
                                    color=ft.colors.RED,
                                    border_color=ft.colors.BLUE_200, 
                                    capitalization="characters",
                                    border=ft.InputBorder.UNDERLINE)

            page.bottom_appbar = ft.BottomAppBar(
                bgcolor=ft.colors.BLUE,
                content=ft.Row(
                    controls=[
                        ft.IconButton(icon=ft.icons.MENU, icon_color=ft.colors.WHITE),
                        ft.Container(expand=True),
                        ft.IconButton(icon=ft.icons.SEARCH, icon_color=ft.colors.WHITE),
                        ft.IconButton(icon=ft.icons.FAVORITE, icon_color=ft.colors.WHITE),
                    ]
                ),
            )

            page.add(text_field_name)

        ft.app(target=main,port=8080, view=None)



- Dockerfile

        ❯ vim Dockerfile

            FROM python:3-alpine

            WORKDIR /app

            COPY requirements.txt ./
            RUN pip install --no-cache-dir -r requirements.txt

            COPY . .

            EXPOSE 8080

            CMD ["python", "./main.py"]


#### Test application with Docker container


    ❯ docker build -t fletapp .

    ❯ docker run -d --name fletapp-avc -p 8080:8080 fletapp



    # list

    ❯ docker images

        REPOSITORY   TAG       IMAGE ID       CREATED         SIZE
        fletapp      latest    04b55dd3acb2   7 seconds ago   143MB


    ❯ docker ps -a --format "table {{.ID}}\t{{.Image}}\t{{.Status}}\t{{.Names}}\t{{.Ports}}"

        CONTAINER ID   IMAGE     STATUS         NAMES         PORTS
        b1f9de1944fb   fletapp   Up 6 seconds   fletapp-avc   0.0.0.0:8080->8080/tcp


#### Result :

<p align="center">
    <img src="./gambar-petunjuk/ss_app_container_1.png" alt="ss_app_container_1" style="display: block; margin: 0 auto;">
</p>


#### Reset containers :

    ❯ docker rm -f $(docker ps -aq) && docker rmi -f $(docker images -q)

        b1f9de1944fb
        Untagged: fletapp:latest
        Deleted: sha256:04b55dd3acb2588f5f6f0620e8a8730c1f139d397ae197b553d3934644811084

---

<p align="center">
    <img src="./gambar-petunjuk/fly-io-logo.svg" alt="fly-io-logo" style="display: block; margin: 0 auto;">
</p>


---

## Stages in deploying the application to fly.io

#### code :

- toml [Tom's Obvious Minimal Language]


        ❯ vim fly.toml


            app = "damvflettextfield"

            kill_signal = "SIGINT"
            kill_timeout = 5
            processes = []

            [env]
            FLET_SERVER_PORT = "8080"

            [experimental]
            allowed_public_ports = []
            auto_rollback = true

            [[services]]
            http_checks = []
            internal_port = 8080
            processes = ["app"]
            protocol = "tcp"
            script_checks = []

            [services.concurrency]
                hard_limit = 25
                soft_limit = 20
                type = "connections"

            [[services.ports]]
                force_https = true
                handlers = ["http"]
                port = 80

            [[services.ports]]
                handlers = ["tls", "http"]
                port = 443

            [[services.tcp_checks]]
                grace_period = "1s"
                interval = "15s"
                restart_limit = 0
                timeout = "2s"


#### check version :

    ❯ flyctl version

        flyctl v0.2.15 darwin/arm64 Commit: 846630217aff135b32ec0d6a018cf6bdde0f1762 BuildDate: 2024-03-10T09:52:28Z

### &#x1F530; create Apps :

    ❯ flyctl apps create --name damvflettextfield

        automatically selected personal organization: abumuhammad
        New app created: damvflettextfield


check and watch for updates on the fly.io console dashboard (https://fly.io/dashboard)

<p align="center">
    <img src="./gambar-petunjuk/ss_dashboard_app_1.png" alt="ss_dashboard_app_1" style="display: block; margin: 0 auto;">
</p>

### &#x1F530; deploy Apps :

    ❯ flyctl deploy

check and watch for updates on the fly.io console dashboard (https://fly.io/dashboard)

### &#x1F530; check

### &#x1F530; open :

---

<p align="center">
    <img src="./gambar-petunjuk/well_done.png" alt="well_done" style="display: block; margin: 0 auto;">
</p>


---


### delete apps