import ssl
import socket
import sys

TARGETS = ["api.opencode.ai", "api.github.com", "models.dev"]

def check_target(host: str) -> str:
    try:
        ctx = ssl.create_default_context()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(10)
            with ctx.wrap_socket(sock, server_hostname=host) as tls:
                tls.connect((host, 443))
                cert = tls.getpeercert()
                issuer = dict(x[0] for x in cert["issuer"])
                org = issuer.get("organizationName", "unknown")
                subj = dict(x[0] for x in cert["subject"])
                cn = subj.get("commonName", "unknown")
                return f"{host:25s} → Issuer: {org:30s} CN: {cn}"
    except ssl.SSLCertVerificationError as e:
        return f"{host:25s} → SSL ERROR (cert not trusted): {e}"
    except Exception as e:
        return f"{host:25s} → ERROR: {e}"

def main():
    print(f"Python {sys.version}")
    print(f"Certificate store: {ssl.get_default_verify_paths().openssl_cafile}")
    print()

    for target in TARGETS:
        print(check_target(target))

    print()
    print("If Issuer is your company → SSL inspection is ON")
    print("If Issuer is a public CA (Let's Encrypt, DigiCert, etc.) → direct TLS")

if __name__ == "__main__":
    main()
