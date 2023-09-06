# Folder architecture

@TODO

The code is divided in so-called `apps`, a simple separation by business logic. If you are new to the code please take a look at [the example app](/src/apps/example).

To create a new app you can copy the example app in [`src/apps/example`](/src/apps/example). After that you'll just need to follow these steps:
 - Modify the tag of the `Router` object in `src/apps/<your_app>/api.py`.
 - Add your app's functionality under a custom route in `src/config/api.py`.
 - Add your app to the installed apps in `src/config/settings.py`.
 - Modify `src/apps/<your_app>/apps.py` by changing the name of the class and the exported name.
