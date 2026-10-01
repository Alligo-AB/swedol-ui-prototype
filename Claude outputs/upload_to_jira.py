#!/usr/bin/env python3
"""
Jira Attachment Uploader - Upload PNG files to Jira issue AE-3512
This script uploads design review comparison images to the Jira ticket.

Usage:
    python3 upload_to_jira.py

Requirements:
    - Python 3.6+
    - requests library (pip install requests)
    - Jira Cloud access via API token
"""

import os
import sys
import requests
from pathlib import Path
from typing import List, Tuple

# Configuration
JIRA_DOMAIN = "alligo.atlassian.net"
ISSUE_KEY = "AE-3512"
FILES_DIR = Path("/mnt/user-data/outputs")

FILES_TO_UPLOAD = [
    "AE-3512-Issue-BorderRadius.png",
    "AE-3512-Issue-Cursor.png",
    "AE-3512-Issue-FontFamily.png",
    "AE-3512-Issue-FontSizeAndPadding.png",
    "AE-3512-Summary-Comparison.png",
]

def upload_attachments(email: str, api_token: str) -> Tuple[List[str], List[str]]:
    """
    Upload PNG files to Jira issue.

    Args:
        email: Atlassian cloud email
        api_token: Jira API token (generate at https://id.atlassian.com/manage/api-tokens)

    Returns:
        Tuple of (successful_uploads, failed_uploads)
    """

    base_url = f"https://{JIRA_DOMAIN}"
    endpoint = f"{base_url}/rest/api/3/issue/{ISSUE_KEY}/attachments"

    # Set up authentication
    auth = (email, api_token)
    headers = {
        "X-Atlassian-Token": "nocheck"
    }

    successful = []
    failed = []

    print(f"\n🚀 Starting upload to Jira issue {ISSUE_KEY}")
    print(f"📍 Endpoint: {endpoint}")
    print(f"📂 Files directory: {FILES_DIR}\n")

    for filename in FILES_TO_UPLOAD:
        filepath = FILES_DIR / filename

        if not filepath.exists():
            print(f"❌ File not found: {filepath}")
            failed.append((filename, "File not found"))
            continue

        try:
            # Read file
            with open(filepath, 'rb') as f:
                file_data = f.read()

            # Get file size
            file_size_kb = filepath.stat().st_size / 1024

            print(f"📤 Uploading {filename} ({file_size_kb:.1f} KB)... ", end="", flush=True)

            # Upload file
            files = {
                'file': (filename, file_data, 'image/png')
            }

            response = requests.post(
                endpoint,
                files=files,
                headers=headers,
                auth=auth,
                timeout=30
            )

            if response.status_code in [200, 201]:
                print(f"✅ Success")
                successful.append(filename)
            else:
                error_msg = f"HTTP {response.status_code}"
                try:
                    error_detail = response.json().get('errorMessages', [response.text])
                    if isinstance(error_detail, list):
                        error_msg = "; ".join(error_detail[:1])
                except:
                    error_msg = response.text[:100]

                print(f"❌ Failed ({error_msg})")
                failed.append((filename, error_msg))

        except Exception as e:
            print(f"❌ Error: {str(e)}")
            failed.append((filename, str(e)))

    return successful, failed

def main():
    """Main entry point."""

    print("=" * 60)
    print("Jira Attachment Uploader")
    print("=" * 60)

    # Check if files exist
    missing_files = [f for f in FILES_TO_UPLOAD if not (FILES_DIR / f).exists()]
    if missing_files:
        print(f"\n❌ Error: Missing files:")
        for f in missing_files:
            print(f"   - {f}")
        return 1

    print(f"\n✓ Found all {len(FILES_TO_UPLOAD)} files to upload")

    # Get credentials
    print("\n🔐 Authentication required:")
    print("   You need your Jira API token to continue.")
    print("   Generate one at: https://id.atlassian.com/manage/api-tokens")
    print("   (It's NOT your password)\n")

    email = input("Enter your Atlassian email: ").strip()
    if not email:
        print("❌ Email is required")
        return 1

    import getpass
    api_token = getpass.getpass("Enter your Jira API token: ")
    if not api_token:
        print("❌ API token is required")
        return 1

    # Upload files
    successful, failed = upload_attachments(email, api_token)

    # Print summary
    print("\n" + "=" * 60)
    print("📊 Upload Summary")
    print("=" * 60)
    print(f"✅ Successful: {len(successful)}/{len(FILES_TO_UPLOAD)}")
    print(f"❌ Failed: {len(failed)}/{len(FILES_TO_UPLOAD)}")

    if successful:
        print(f"\nSuccessfully uploaded:")
        for f in successful:
            print(f"   ✓ {f}")

    if failed:
        print(f"\nFailed uploads:")
        for f, reason in failed:
            print(f"   ✗ {f} - {reason}")

    # Print result
    print("\n" + "=" * 60)
    if failed:
        print(f"⚠️  {len(failed)} file(s) failed to upload")
        print("\n🔍 Troubleshooting:")
        print("   1. Check your email and API token")
        print("   2. Ensure you have permission to add attachments to this issue")
        print("   3. Try again with correct credentials")
        return 1
    else:
        print(f"🎉 All {len(successful)} files uploaded successfully!")
        print(f"\n✨ Your design review comparison images are now attached to:")
        print(f"   https://{JIRA_DOMAIN}/browse/{ISSUE_KEY}")
        return 0

if __name__ == "__main__":
    sys.exit(main())
