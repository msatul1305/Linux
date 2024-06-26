- To get list of all packages available in venv - pip freeze
- Python test discovery
    - test_*.py, *_test.py files
- Python config file
    - create Pytest.ini under root folder and add the following properties to override the path of directory to look for test files:
        - testpaths=tests
- FOR CS ENV: Add artifactory link in ".ini" file inside venv folder to download packages from artifactory instead of internet.
- All test functions and test file must have method name test_* or *_test. Class names: Test*.
- FIXTURES:
    -  runs for every function/test - similar to setup/teardown
    -  starts with @pytest.fixture
    -  can have scope: function, class, module, package, session.
    -  if scope = class, fixture will run each time a class is called.
    -  eg. fixt.py
- Markers
    - used to set features/attributes to test functions
    - types of markers:
    - @pytest.mark.xfail: donot give details of why test failed
    - @pytest.mark.skip: skip this test
    - @pytest.mark.parametrize: to test/run against multiple inputs
    - CUSTOM MARKERS(self added markers - warning need to be supressed and marker need to be registered to use): @pytest.mark.common
