from errbot import BotPlugin, botcmd, arg_botcmd, webhook


class Covid19helpbot(BotPlugin):
    """
    This bot will help you find things you require during this pandemic.
    """

    # def activate(self):
    #     """
    #     Triggers on plugin activation

    #     You should delete it if you're not using it to override any default behaviour
    #     """
    #     super(Covid19helpbot, self).activate()

    # def deactivate(self):
    #     """
    #     Triggers on plugin deactivation

    #     You should delete it if you're not using it to override any default behaviour
    #     """
    #     super(Covid19helpbot, self).deactivate()

    # def get_configuration_template(self):
    #     """
    #     Defines the configuration structure this plugin supports

    #     You should delete it if your plugin doesn't use any configuration like this
    #     """
    #     return {'EXAMPLE_KEY_1': "Example value",
    #             'EXAMPLE_KEY_2': ["Example", "Value"]
    #            }

    # def check_configuration(self, configuration):
    #     """
    #     Triggers when the configuration is checked, shortly before activation

    #     Raise a errbot.ValidationException in case of an error

    #     You should delete it if you're not using it to override any default behaviour
    #     """
    #     super(Covid19helpbot, self).check_configuration(configuration)

    # def callback_connect(self):
    #     """
    #     Triggers when bot is connected

    #     You should delete it if you're not using it to override any default behaviour
    #     """
    #     pass

    # def callback_message(self, message):
    #     """
    #     Triggered for every received message that isn't coming from the bot itself

    #     You should delete it if you're not using it to override any default behaviour
    #     """
    #     pass

    # def callback_botmessage(self, message):
    #     """
    #     Triggered for every message that comes from the bot itself

    #     You should delete it if you're not using it to override any default behaviour
    #     """
    #     pass

    @webhook
    def example_webhook(self, incoming_request):
        """A webhook which simply returns 'Example'"""
        return "Example"

    # Passing split_args_with=None will cause arguments to be split on any kind
    # of whitespace, just like Python's split() does
    @botcmd(split_args_with=None)
    def saycovid(self, message, args):
        """A command which simply returns 'Example'"""
        return "Covid"

    @arg_botcmd('name', type=str)
    @arg_botcmd('--favorite-number', type=int, unpack_args=False)
    def say_hello(self, message, args):
        """
        A command which says hello to someone.

        If you include --favorite-number, it will also tell you their
        favorite number.
        """
        if args.favorite_number is None:
            return f'Hello {args.name}.'
        else:
            return f'Hello {args.name}, I hear your favorite number is {args.favorite_number}.'

    def _all_hospitals(self, args):
        city = args.city
        return f'All hospitals in {city}'
    
    def _o2_hospitals(self, args):
        city = args.city
        return f'O2 hospitals in {city}'

    def _ventilator_hospitals(self, args):
        city = args.city
        return f'Ventilator hospitals in {city}'
    
    def _icu_hospitals(self, args):
        city = args.city
        return f'ICU hospitals in {city}'

    def _hospital_data(self, args):
        atleast_switcher = {
            "all"           : self._all_hospitals,
            "O2"            : self._o2_hospitals,
            "Ventilator"    : self._ventilator_hospitals,
            "ICU"           : self._icu_hospitals
        }

        _get_hospitals = atleast_switcher.get(args.atleast, lambda :'Invalid choice')

        return _get_hospitals(args)

    @arg_botcmd('city', type=str)
    @arg_botcmd('--atleast', type=str, default="all", unpack_args=False)
    def hospitals(self, message, args):
        """
        This command finds the hospitals with beds in the give city.

        Default is get all hospitals with any type of beds available.
        --atleast O2            : Hospitals with at least O2 beds available
        --atleast Ventilatore   : Hospitals with at least Ventilator beds available
        --atleast ICU           : Hospitals with at least ICU  beds available
        """
        return self._hospital_data(args)
    
    

