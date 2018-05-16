import simpy


class Car(object):
    def __init__(self, env):
        self.env = env
        self.action = env.process(self.run())

    def run(self):
        while True:
            print("Start parking and charging at %d" % self.env.now)
            charge_duration = 5
            try:
                yield self.env.process(self.charge(charge_duration))
            except simpy.Interrupt:
                print('Was interrupted. Hope the battery was full enough ...')

            print('Start driving at %d' % self.env.now)
            trip_duration = 2
            yield self.env.timeout(trip_duration)

    def charge(self, duration):
        yield self.env.timeout(duration)



if __name__ == '__main__':

    #Create a RBtree
    #env = simpy.Environment()
    #env.process(car(env))
    #env.run(until=15)

    env = simpy.Environment()
    car = Car(env)
    env.run(until=15)

