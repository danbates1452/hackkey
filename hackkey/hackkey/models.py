# Database Models
from django.db import models
from django.core.validators import MinValueValidator

REASONABLE_MAX_STRING_LENGTH = 128

class Users(models.Model):
    DARK = "dark"
    LIGHT = "light"
    BLUE = "blue"
    LIGHTBLUE = "lightblue"
    GREY = "grey"
    GREEN = "green"
    RED = "red"
    YELLOW = "yellow"

    THEME_CHOICES = {
        DARK: "Dark",
        LIGHT: "Light",
        BLUE: "Blue",
        LIGHTBLUE: "Light Blue",
        GREY: "Grey",
        GREEN: "Green",
        RED: "Red",
        YELLOW: "Yellow",
    }

    # user field (user's id) is autogenerated by django
    email_address = models.EmailField(max_length=REASONABLE_MAX_STRING_LENGTH)
    password = models.CharField(max_length=REASONABLE_MAX_STRING_LENGTH)
    logged_in_today = models.BooleanField(default=True)
    login_daily_claimed = models.BooleanField(default=False)
    selected_theme = models.CharField(
        max_length=max([len(stored_val) for stored_val, _ in THEME_CHOICES.items()]),
        choices=THEME_CHOICES.items(),
        default=DARK,
    )
    rolls_owned = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])

class Entries(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    entry_id = models.CharField(max_length=REASONABLE_MAX_STRING_LENGTH)
    username = models.CharField(max_length=REASONABLE_MAX_STRING_LENGTH)
    password = models.CharField(max_length=REASONABLE_MAX_STRING_LENGTH) #hashed
    uri = models.CharField(max_length=REASONABLE_MAX_STRING_LENGTH) #todo: expand to having multiple URIs

class PremiumFeatures(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    enhanced_password_generation = models.BooleanField('Enhanced Password Generation')

class GachaRewards(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    # themes
    dark_theme = models.BooleanField('Dark Theme', default=False)
    light_theme = models.BooleanField('Light Theme', default=False)
    blue_theme = models.BooleanField('Blue Theme', default=False)
    lightblue_theme = models.BooleanField('Light Blue Theme', default=False)
    grey_theme = models.BooleanField('Grey Theme', default=False)
    green_theme = models.BooleanField('Green Theme', default=False)
    red_theme = models.BooleanField('Red Theme', default=False)
    yellow_theme = models.BooleanField('Yellow Theme', default=False)

