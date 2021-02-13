FROM ruby:2.6-slim

RUN bundle config --global frozen 1

WORKDIR /usr/src/app

COPY Gemfile Gemfile.lock ./

RUN gem install bundler:2.2.9

RUN bundle install

COPY main.rb .

CMD ["ruby","main.rb"]