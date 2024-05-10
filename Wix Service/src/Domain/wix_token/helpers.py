def generate_install_redirect_url(token: str):
    app_id="7b209384-e657-4b59-b92e-54e61d3fafec"
    REDIRECT_URL="https://www.google.com/"
    redirect_url = f"https://www.wix.com/installer/install?token={token}&appId={app_id}&redirectUrl={REDIRECT_URL}"
    print('redirect_url', redirect_url)
    return redirect_url