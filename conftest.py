import pytest
import os
from datetime import datetime
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720}
    }

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook that intercepts test execution results nad Captures full-page screenshots for all tests (Passed or Failed).
    """

    outcome = yield # means Let the test execution phase complete first
    report = outcome.get_result()
    
    #  Capturing a screenshot immediately after the main test function ('call' phase) finishes
    if report.when == "call":

        page = item.funcargs.get("page")
        if page:
            screenshot_dir = os.path.join(item.config.rootdir, "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)
            
            status = "FAILED" if report.failed else "PASSED"
            
            # ss file name
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            clean_test_name = item.name.replace("[", "_").replace("]", "_")
            screenshot_path = os.path.join(
                screenshot_dir, 
                f"{clean_test_name}_{status}_{timestamp}.png"
            )
            
            page.screenshot(path=screenshot_path, full_page=True)