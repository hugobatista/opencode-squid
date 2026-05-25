from proxy import Proxy

if __name__ == "__main__":
    print("Starting proxy on 127.0.0.1:3128...")
    print("Point HTTPS_PROXY=http://127.0.0.1:3128 in opencode")
    print("Press Ctrl+C to stop")
    Proxy(hostname="127.0.0.1", port=3128).start()
