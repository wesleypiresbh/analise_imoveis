mkedir -p ~/.streamlit/

echo "\
[general]\n\
email= \"wesleypiresbh@gmail.com\"\n\
"> ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\n
enableCORS=false\n\
port = SPORT\n\
" > ~/.streamlit/config.toml


