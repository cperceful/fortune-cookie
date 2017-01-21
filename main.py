#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import random;

def getRandomFortune():
    #list of possible fortunes
    fortunes = [
        "You will find true love on flag day",
        "Help I'm trapped in a computer",
        "Invest in Segway"
    ];

    #randomly select one of the fortunes
    return random.choice(fortunes);

class MainHandler(webapp2.RequestHandler):

    def get(self):
        header = "<h1>Fortune Cookie</h1>";

        fortune = "<strong>" + str(getRandomFortune()) + "</strong>"
        fortuneSentence = "<p>Your fortune: {}</p>".format(fortune);

        luckyNumber = "<strong>" + str(random.randint(1, 100)) + "</strong>"
        numberSentence = '<p>Your lucky number is {}</p>'.format(luckyNumber);

        button = '<a href="."><button>New cookie pls</button></a>'

        self.response.write(header + fortuneSentence + numberSentence + button);






app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)
