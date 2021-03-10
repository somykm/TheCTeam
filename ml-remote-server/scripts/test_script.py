import tensorflow as tf
import unreal_engine as ue  # for remote logging only
from mlpluginapi import MLPluginAPI


class TestScriptAPI(MLPluginAPI):

    # expected optional api: setup your model for training
    def on_setup(self):
        pass

    # expected optional api: parse input object and return a result object, which will be converted to json for UE4
    def on_json_input(self, json_input):

        ue.log(json_input)
        
        return {'a': 2}

    # custom function to change the op
    def change_operation(self, type):
        pass

    # expected optional api: start training your network
    def on_begin_training(self):
        pass


# NOTE: this is a module function, not a class function. Change your CLASSNAME to reflect your class
# required function to get our api
def get_api():
    # return CLASSNAME.get_instance()
    return TestScriptAPI.get_instance()