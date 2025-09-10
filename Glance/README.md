# Auto Setup
```yml
mkdir glance && cd glance && curl -sL https://github.com/glanceapp/docker-compose-template/archive/refs/heads/main.tar.gz | tar -xzf - --strip-components 2
```
With `sudo`
```yml
sudo mkdir glance && cd glance && sudo curl -sL https://github.com/glanceapp/docker-compose-template/archive/refs/heads/main.tar.gz | sudo tar -xzf - --strip-components 2
```
# Manual Setup
## Docker Compose
- CD into a desired app directory
- Create your docker-compose.yml
```yml
    image: glanceapp/glance
    restart: unless-stopped
    volumes:
      - ./config:/app/config
      - ./assets:/app/assets
      - /etc/localtime:/etc/localtime:ro
      # Optionally, also mount docker socket if you want to use the docker containers widget
      # - /var/run/docker.sock:/var/run/docker.sock:ro
    ports:
      - 8080:8080
    env_file: .env
```
# Config files
Create a `config` directory next to your docker-compose.yml
```bash
mkdir config
```
Save `config/glance.yml`
```yml
pages:
  - name: Home
    # Optionally, if you only have a single page you can hide the desktop navigation for a cleaner look
    # hide-desktop-navigation: true
    columns:
      - size: small
        widgets:
          - type: calendar
            first-day-of-week: monday

          - type: rss
            limit: 10
            collapse-after: 3
            cache: 12h
            feeds:
              - url: https://selfh.st/rss/
                title: selfh.st
                limit: 4
              - url: https://ciechanow.ski/atom.xml
              - url: https://www.joshwcomeau.com/rss.xml
                title: Josh Comeau
              - url: https://samwho.dev/rss.xml
              - url: https://ishadeed.com/feed.xml
                title: Ahmad Shadeed

          - type: twitch-channels
            channels:
              - theprimeagen
              - j_blow
              - piratesoftware
              - cohhcarnage
              - christitustech
              - EJ_SA

      - size: full
        widgets:
          - type: group
            widgets:
              - type: hacker-news
              - type: lobsters

          - type: videos
            channels:
              - UCXuqSBlHAE6Xw-yeJA0Tunw # Linus Tech Tips
              - UCR-DXc1voovS8nhAvccRZhg # Jeff Geerling
              - UCsBjURrPoezykLs9EqgamOA # Fireship
              - UCBJycsmduvYEL83R_U4JriQ # Marques Brownlee
              - UCHnyfMqiRRG1u-2MsSQLbXA # Veritasium

          - type: group
            widgets:
              - type: reddit
                subreddit: technology
                show-thumbnails: true
              - type: reddit
                subreddit: selfhosted
                show-thumbnails: true

      - size: small
        widgets:
          - type: weather
            location: London, United Kingdom
            units: metric # alternatively "imperial"
            hour-format: 12h # alternatively "24h"
            # Optionally hide the location from being displayed in the widget
            # hide-location: true

          - type: markets
            markets:
              - symbol: SPY
                name: S&P 500
              - symbol: BTC-USD
                name: Bitcoin
              - symbol: NVDA
                name: NVIDIA
              - symbol: AAPL
                name: Apple
              - symbol: MSFT
                name: Microsoft

          - type: releases
            cache: 1d
            # Without authentication the Github API allows for up to 60 requests per hour. You can create a
            # read-only token from your Github account settings and use it here to increase the limit.
            # token: ...
            repositories:
              - glanceapp/glance
              - go-gitea/gitea
              - immich-app/immich
              - syncthing/syncthing

  # Add more pages here:
  # - name: Your page name
  #   columns:
  #     - size: small
  #       widgets:
  #         # Add widgets here

  #     - size: full
  #       widgets:
  #         # Add widgets here

  #     - size: small
  #       widgets:
  #         # Add widgets here
```
Save `config/home.yml`
```yml
- name: Home
  # Optionally, if you only have a single page you can hide the desktop navigation for a cleaner look
  # hide-desktop-navigation: true
  columns:
    - size: small
      widgets:
        - type: calendar
          first-day-of-week: monday

        - type: rss
          limit: 10
          collapse-after: 3
          cache: 12h
          feeds:
            - url: https://selfh.st/rss/
              title: selfh.st
            - url: https://ciechanow.ski/atom.xml
            - url: https://www.joshwcomeau.com/rss.xml
              title: Josh Comeau
            - url: https://samwho.dev/rss.xml
            - url: https://ishadeed.com/feed.xml
              title: Ahmad Shadeed

        - type: twitch-channels
          channels:
            - theprimeagen
            - j_blow
            - giantwaffle
            - cohhcarnage
            - christitustech
            - EJ_SA

    - size: full
      widgets:
        - type: group
          widgets:
            - type: hacker-news
            - type: lobsters

        - type: videos
          channels:
            - UCXuqSBlHAE6Xw-yeJA0Tunw # Linus Tech Tips
            - UCR-DXc1voovS8nhAvccRZhg # Jeff Geerling
            - UCsBjURrPoezykLs9EqgamOA # Fireship
            - UCBJycsmduvYEL83R_U4JriQ # Marques Brownlee
            - UCHnyfMqiRRG1u-2MsSQLbXA # Veritasium

        - type: group
          widgets:
            - type: reddit
              subreddit: technology
              show-thumbnails: true
            - type: reddit
              subreddit: selfhosted
              show-thumbnails: true

    - size: small
      widgets:
        - type: weather
          location: London, United Kingdom
          units: metric # alternatively "imperial"
          hour-format: 12h # alternatively "24h"
          # Optionally hide the location from being displayed in the widget
          # hide-location: true

        - type: markets
          markets:
            - symbol: SPY
              name: S&P 500
            - symbol: BTC-USD
              name: Bitcoin
            - symbol: NVDA
              name: NVIDIA
            - symbol: AAPL
              name: Apple
            - symbol: MSFT
              name: Microsoft

        - type: releases
          cache: 1d
          # Without authentication the Github API allows for up to 60 requests per hour. You can create a
          # read-only token from your Github account settings and use it here to increase the limit.
          # token: ...
          repositories:
            - glanceapp/glance
            - go-gitea/gitea
            - immich-app/immich
            - syncthing/syncthing
```
