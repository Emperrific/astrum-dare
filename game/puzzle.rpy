init python:

    class Processor:
        def __init__(self, name, units, limits):
            self.length = len_unit * units
            self.name = name
            self.units = units
            self.limits = limits
            self.schedule = []
            self.active = False
            all_processors.append(self)

        def can_add(self, new_task, pos):
            if not self.active:
                return False
            if pos < 0:
                return False
            if pos + new_task.units > self.units:
                return False
            for (task, start) in self.schedule:
                end = start + task.units
                if start <= pos and end > pos: #current task begins before new one, must end before it too or overlap
                    return False
                if pos < start and pos + new_task.units > start: #new task begins before current on, must end before it too or overlap
                    return False
            return True #if nothing is wrong then we can do it

        def add(self, new_task, pos):
            if self.can_add(new_task, pos):
                self.schedule.append((new_task, pos))
                new_task.processor = self
                new_task.start = pos
                print("added")
                return True
            print("couldn't add")
            return False

        def unschedule(self, to_remove):
            if to_remove.processor != self or to_remove.start is None:
                return
            if (to_remove, to_remove.start) in self.schedule:
                self.schedule.remove((to_remove, to_remove.start))
                to_remove.processor = None
                to_remove.start = None

        def clear_schedule(self):
            for (task, start) in self.schedule:
                task.processor = None
                task.start = None
            self.schedule = []

        def valid(self):
            for(task, start) in self.schedule:
                end = start + task.units
                if end > self.limits[num_active-1]:
                    print ("Gone over limit: {} ends at {} but was required to end before {}".format(task.name, end, self.limits[num_active]))
                    return False
            return True

        def process_drop(self, dropped, drags):
            x = drags[0].x - dropped.x
            pos = x * self.units / self.length
            if self.add(current_drag, pos):
                drags[0].snap(dropped.x + pos * len_unit + 5+10, dropped.y+5+15, .3)
            else:
                drags[0].snap(renpy.random.randint(100,500), renpy.random.randint(100,300), .3)

    def turn_on(processor):
        if processor.active:
            return
        processor.active = True
        store.num_active += 1

    def turn_off(processor):
        if not processor.active:
            return
        processor.active = False
        store.num_active -= 1

    class Task:
        def __init__(self, name, units, color, dependencies=[]):
            self.name = name
            self.units = units
            self.color = color
            self.dependencies = dependencies
            self.processor = None
            self.start = None
            all_tasks.append(self)

        def valid(self):
            if self.processor is None:
                print ("no processor")
                return False
            for task in self.dependencies:
                if not task.valid() or not task.before(self):
                    print ("failed dependency: {}".format(task.name))
                    return False
            return True

        def before(self, other):
            return (not self.start is None) and (not other.start is None) and self.start + self.units <= other.start

        def set_dragged(self, drags, drop):
            store.current_drag = self
            if self.processor:
                self.processor.unschedule(self)

        def get_dep_str(self):
            if not len(self.dependencies):
                return None
            return "{} follows {}".format(self.name, ", ".join((d.name for d in self.dependencies)))

    all_processors = []
    all_tasks = []

    def find_processor(name):
        for processor in all_processors:
            if processor.name == name:
                return processor
        return None

    def find_task(name):
        for task in all_tasks:
            if task.name == name:
                return task
        return None

    def valid_puzzle(processors, tasks):
        for processor in processors:
            print ("p {} {}".format(processor.name, processor.valid()))
            if not processor.valid():
                return False
        for task in tasks:
            print ("t {} {}".format(task.name, task.valid()))
            if not task.valid():
                return False
        print ("valid")
        return True


transform delayed_fall_in(t=0):
    rotate_pad False
    rotate -4
    alpha 0.0
    zoom 1.3
    offset (-200, -100)
    pause t
    easein 1 alpha 1 zoom 1 rotate 0 offset (0,0)

transform sweep(startx, starty, endx):
    xpos startx
    ypos starty
    linear 10.0 xpos endx

default num_active = 0
define len_unit = 50
default current_drag = None

screen puzzle_sweep(startx, starty, endx, height, failed=False, processors=[], tasks=[]):
    zorder 50

    add "#000":
        at sweep(startx, starty, endx)
        size(10,height)

    if failed:
        timer 10 action Show("fail_sweep", None, starty, endx, height)
    timer 10.5 action [Hide("puzzle_sweep"), Return(Function(valid_puzzle, processors, tasks))]

screen fail_sweep(starty, endx, height):
    zorder 51

    add "#f00":
        pos (endx, starty)
        size(10,height)
    timer 0.5 action Hide("fail_sweep")

screen pipeline_puzzle(processors=[], tasks=[], time=0):
    #add "#fff"

    if time > 0:
        timer time action Return("timeout")

    frame:
        at delayed_fall_in
        xalign 0.9
        yalign 0.9
        textbutton "Launch":
            action Show("puzzle_sweep", None, 50, 200, 400, 200, True, processors, tasks)

    frame:
        at delayed_fall_in
        xalign 0.37
        yalign 0.9
        $time_allowed = processors[0].limits[num_active]
        text "Available Time Before Lockdown: [time_allowed]"

    vbox:
        at delayed_fall_in
        xalign 0.9
        yalign 0.1
        xmaximum 500

        frame:
            vbox:
                text "Schedule all protocol blocks on active cores to override security."
                text "All cores run together, but the total allowed time {color=#f00}decreases{/color} with the number of active cores."

        null height 20
        frame:
            text "Any protocol running before all its prerequisites finish will trigger failure."
            
        null height 20
        frame:    
            text "Hit Launch once configuration is complete to start security override."

        null height 20
        frame:
            xalign 1.0
            vbox:
                text "Requirements: "
                for task in tasks:
                    $s = task.get_dep_str()
                    if s:
                        text s


    draggroup:
        at delayed_fall_in
        for i in range(len(tasks)):
            $task = tasks[i]
            drag:
                xpos 50 + (i%2)*350
                ypos 50 + (i/2) *30
                drag_name task.name
                droppable False
                dragged task.set_dragged
                fixed:
                    xysize(len_unit * task.units, 20)
                    add task.color:
                        size(len_unit * task.units, 20)
                    text task.name:
                        color "#000"
                        xoffset 20
                        yoffset -3

        for i in range(len(processors)):
            $processor = processors[i]
            $num_units = processor.limits[num_active-1]
            $processor_length = num_units * len_unit
            $red_length = processor.length - processor_length
            drag:
                xpos 50
                ypos 500 -(len(processors)/2*50) + i * 50
                drag_name processor.name
                draggable False
                dropped processor.process_drop
                frame:
                    fixed:
                        offset (10,10)
                        xysize(processor_length+red_length+(180 if i>0 else 40), 50)
                        $p_color = "#555"
                        if processor.active:
                            $p_color = "#fff"
                        add p_color:
                            size(processor_length, 10)
                            pos(0,10)
                        add "#e11":
                            size(red_length,10)
                            pos(processor_length,10)
                        add "#e11":
                            size(10,30)
                            pos(processor.length,0)
                        for j in range(num_units+1):
                            add p_color:
                                size(10,30)
                                pos((j * processor_length)/num_units,0)
                        if i > 0:
                            frame:
                                xalign 1.0
                                hbox:
                                    spacing 20
                                    style_prefix "radio"
                                    textbutton "On":
                                        #text_color "#000"
                                        action Function(turn_on, processor)
                                        selected (processor.active)
                                    textbutton "Off":
                                        #text_color "#000"
                                        action Function(turn_off, processor)
                                        selected not processor.active
