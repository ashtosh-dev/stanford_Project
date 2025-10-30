from playwright.sync_api import sync_playwright

def handle_console(msg):
    print(f"Browser console: {msg.text}")

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()

    page.on("console", handle_console)

    page.goto("http://localhost:5173")
    try:
        page.locator("text=Sports").click(timeout=5000)
        page.screenshot(path="jules-scratch/verification/quiz-app.png")
    except Exception as e:
        print(f"Playwright error: {e}")
    finally:
        browser.close()

with sync_playwright() as p:
    run(p)
