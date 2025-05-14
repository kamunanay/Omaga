import os
import re
import subprocess
import requests
import speedtest
from pythonping import ping as pping

def get_public_ip_info():
    try:
        token = os.getenv('IPINFO_TOKEN')
        url = f"https://ipinfo.io{'/json' if not token else f'?token={token}'}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": f"Gagal mendapatkan info IP: {str(e)}"}

def get_provider(org):
    provider_mapping = {
        'Telkomsel': ['Telkomsel', 'AS23693'],
        'Indosat Ooredoo': ['Indosat', 'AS23694', 'IM2'],
        'XL Axiata': ['XL', 'AS24284'],
        '3 (Tri)': ['Tri', 'AS9881', '3'],
        'Smartfren': ['Smartfren', 'AS24235'],
        'Axis': ['Axis', 'AS23866'],
        'By.U': ['NTS', 'AS5555']
    }
    
    if not org:
        return 'Unknown'
    
    for provider, keywords in provider_mapping.items():
        for keyword in keywords:
            if keyword.lower() in org.lower():
                return provider
    return 'Unknown'

def check_ping(host):
    try:
        result = pping(host, count=3, timeout=2)
        return f"{result.rtt_avg_ms:.2f} ms" if result.success() else 'N/A'
    except Exception:
        return 'N/A'

def run_speedtest():
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download = st.download() / 1_000_000  # Convert to Mbps
        upload = st.upload() / 1_000_000
        ping = st.results.ping
        return download, upload, ping
    except Exception as e:
        return None, None, None
