FROM nginx:1.13.3

RUN rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/

RUN rm /etc/nginx/conf.d/default.conf
COPY project.conf /etc/nginx/conf.d/
ARG PROXY_PASS
RUN sed -i -e "s!proxy_pass_variable!${PROXY_PASS}!g" /etc/nginx/conf.d/project.conf