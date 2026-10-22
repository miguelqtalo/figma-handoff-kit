#!/usr/bin/env python3
"""Hook (PreToolUse): block reading or editing secret files.

Denies any tool call whose path, pattern or command names a .env file,
a key file or a credentials file. Exit 2 blocks the call and tells Claude why.
"""
import json
import re
import sys

SECRET = re.compile(
    r"(^|[\s/'\"=])\.env(\.[\w-]+)?($|[\s'\"])"
    r"|credentials?(\.json|\.ya?ml)?\b"
    r"|secrets?\.(json|ya?ml|toml)\b"
    r"|\.pem\b|\bid_(rsa|ed25519)\b|\.npmrc\b|\.aws/",
    re.IGNORECASE,
)


def main():
    data = json.load(sys.stdin)
    tool_input = data.get("tool_input") or {}
    fields = [str(tool_input.get(k, "")) for k in ("file_path", "path", "pattern", "command", "glob")]
    for value in fields:
        m = SECRET.search(value)
        if m:
            sys.stderr.write(
                f"block-secrets: blocked {data.get('tool_name')} on a secret file ({m.group(0).strip()}). "
                "This kit never reads or edits secrets.\n"
            )
            return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
