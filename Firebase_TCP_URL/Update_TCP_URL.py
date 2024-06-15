import Firebase
import subprocess


def update_tcp_url():
    print("Updating TCP_URL...")
    cmd = "ngrok tcp 5000 --log=stdout"
    p = subprocess.Popen(cmd.split(" "), stdout=subprocess.PIPE)
    while True:
        line_with_ngrok_url = p.stdout.readline().strip().decode("utf-8")
        if line_with_ngrok_url.find("started tunnel") != -1:
            url_only = line_with_ngrok_url[
                line_with_ngrok_url.index("url=") + len("url=") :
            ]
            Firebase.update("/", {"TCP_URL": url_only})
            break
    print("Updating TCP_URL... Done!")


if __name__ == "__main__":
    update_tcp_url()
