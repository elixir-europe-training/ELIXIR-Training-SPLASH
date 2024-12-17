FROM ruby:3.1

ENV LC_ALL C.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

WORKDIR /usr/src/app

COPY Gemfile ./
RUN gem install bundler:2.4.21 && bundle install
RUN gem install racc -v 1.7.1

EXPOSE 4000
