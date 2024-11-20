from selenium import webdriver
from selenium.common.exceptions import NoSuchWindowException, WebDriverException

def test_window_exception():
    with webdriver.Chrome() as driver:
        try:
            # Navigate to Selenium homepage
            driver.get('https://seleniumhq.github.io')

            # Set name for the first tab
            driver.execute_script("window.name = 'Selenium';")

            # Get name of the first tab
            first_tab_name = driver.execute_script("return window.name;")
            print(f'First tab name is: {first_tab_name}')

            # Get page title
            first_tab_title = driver.title
            print(f'First tab title: {first_tab_title}')

            # Open a new tab
            driver.execute_script("window.open('https://www.google.com', '_blank');")

            # Switch to the new tab
            if len(driver.window_handles) > 1:  # Ensure there are multiple tabs
                driver.switch_to.window(driver.window_handles[-1])
                # Set name for new tab
                driver.execute_script("window.name = 'Google';")  

                # Get name of the new tab
                new_tab_name = driver.execute_script("return window.name;")
                print(f'New tab name is: {new_tab_name}')
            else:
                print("No new tab was opened.")

            # Attempt to switch back to the previous tab safely
            if any(handle for handle in driver.window_handles if driver.execute_script("return window.name;") == 'Selenium'):
                # Safely switch by index
                driver.switch_to.window(driver.window_handles[0])  
                assert first_tab_title == driver.title, f'Expected {first_tab_title} as title'
                print("Switched back to the first tab successfully.")
            else:
                print("First tab is not available to switch back to.")
        
        except NoSuchWindowException as e:
            print(f"NoSuchWindowException caught: {e}")
        except WebDriverException as e:
            print(f"WebDriverException caught: {e}")
        except AssertionError as e:
            print(f"AssertionError: {e}")
        finally:
            print("Test execution completed.")
