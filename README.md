# betapostcrawler

This script iterates through the posts of a given facebook page and generates a text file containing a list of <b>unique list facebook id`s</b> who liked the posts. The output is ready to be imported from facebook ads manager to create custom audience.

### Basic Usage - just change the variables ###

    targetId (any facebook page id)
    initialDate/until
    threshold (max number of unique facebook id`s)

### More Authentication Options ###

By default, this script will make all it's requests as the <b>beta_posts_crawler</b> facebook app.
If you want the requests to be made by your own facebook application, you must
modify the APP_ID setting.  For example:

    fbconsole.APP_ID = '<your-app-id>'
    fbconsole.authenticate()

For the authentication flow to work, you must configure your Facebook
application correctly by setting the "Site URL" option to http://local.fbconsole.com:8080

Any doubts on fbconsole please check https://github.com/fbsamples/fbconsole

#### TIP - How to get facebook page id ####

http://findmyfacebookid.com/
