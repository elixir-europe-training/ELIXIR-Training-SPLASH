FROM ruby:3.1

ENV LC_ALL C.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

WORKDIR /usr/src/app

# Copy Gemfile and Gemfile.lock so bundle install during build uses the lockfile
COPY Gemfile Gemfile.lock ./
# install bundler and gems during image build so container has all dependencies
RUN gem install bundler:2.4.21 \
 && bundle config set --local path /usr/local/bundle \
 && bundle install --jobs 4 --retry 3

EXPOSE 4000
