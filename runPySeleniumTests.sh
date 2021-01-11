#!/bin/sh

#Defaults
browser_type="chrome"
smoke=false
docker_container=false
virtualenv_enable=false
email=""
password=""

isVirtualEnvOn () {
    if [[ "$VIRTUAL_ENV" != "" ]]; then
        virtualenv_enable=true
    else
        virtualenv_enable=false
    fi
}

while [[ $# -gt 0 ]]
do
    case "$1" in 
        "-b" | "--browser") 
        shift
        browser_type=$(echo "$1" | awk '{print tolower($0)}');;

        "-s" | "--smoke")
        smoke=true;;

        "-d" | "--docker-container")
        docker_container=true;;

        "--email")
        shift
        email=$1;;

        "--password")
        shift
        password=$1;;

        *)
        echo " Ignored Argument:  $1 "
    esac
        shift
done

strUserEmailPasswordArgs=''
if [ "$email" != "" ] && [ "$password" != "" ]; then
    strUserEmailPasswordArgs=" --email $email --pwd $password"
fi

if [ "$smoke" == true ] && [ "$docker_container" == true ]; then
    echo " Running SMOKE automated tests in DOCKER $browser_type standalone containers"
    docker-compose up -d --build selenium_${browser_type} py_tests_${browser_type}_smoke

elif [ "$smoke" == false ]  && [ "$docker_container" == true ]; then
    echo " Running REGRESSION automated tests in DOCKER $browser_type standalone containers"
    docker-compose up --build selenium_"$browser_type" py_tests_$browser_type

elif [ "$smoke" == true ] && [ "$docker_container" == false ]; then
    isVirtualEnvOn
    echo " Running SMOKE automated tests in $browser_type LOCAL platform."
    if [ "$virtualenv_enable" == true ]; then
        pytest -s -m smoke --localdriver $strUserEmailPasswordArgs --browser $browser_type --alluredir=test_results/allure_results/
    else
        echo " Virtual Environment not detected to run PyTest tests.  Please activate Virtual Environment and try again."
    fi
elif [ "$smoke" == false ] && [ "$docker_container" == false ]; then
    isVirtualEnvOn
    echo " Running REGRESSION automated tests in $browser_type LOCAL platform."
    if [ "$virtualenv_enable" == true ]; then
        pytest -s tests/ --localdriver $strUserEmailPasswordArgs --browser $browser_type --alluredir=test_results/allure_results/
    else
        echo " Virtual Environment not detected to run PyTest tests.  Please activate Virtual Environment and try again."
    fi

fi


