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
                return True
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
                if end > self.limits[num_active]:
                    return False
            return True

        def process_drop(self, dropped, drags):
            x = drags[0].x - dropped.x
            pos = x * self.units / self.length
            if self.add(current_drag, pos):
                drags[0].snap(dropped.x + pos * len_unit + 5, dropped.y+5, 1)
            else:
                drags[0].snap(renpy.random.randint(100,500), renpy.random.randint(100,300), 1)

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
                return False
            for task in self.dependencies:
                if not task.valid() or not task.before(self):
                    return False
            return True

        def before(self, other):
            return (not self.start is None) and (not other.start is None) and self.start + self.units <= other.start

        def set_dragged(self, drags, drop):
            store.current_drag = self
            if self.processor:
                self.processor.unschedule(self)

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
            if not processor.valid():
                return False
        for task in tasks:
            if not task.valid():
                return False
        return True

default num_active = 0
define len_unit = 50
default current_drag = None


screen pipeline_puzzle(processors=[], tasks=[]):
    
    add "#fff"

    textbutton "Launch" xalign 0.9 yalign 0.9 action Return(Function(valid_puzzle, processors, tasks))

    draggroup:
        for i in range(len(tasks)):
            $task = tasks[i]
            drag:
                xpos 100
                ypos 100 + i *30
                drag_name task.name
                droppable False
                dragged task.set_dragged
                add task.color:
                    size(len_unit * task.units, 20)

        for i in range(len(processors)):
            $processor = processors[i]
            $num_units = processor.limits[num_active-1]
            $processor_length = num_units * len_unit
            $red_length = processor.length - processor_length
            drag:
                xpos 100
                ypos 500 + i * 50
                drag_name processor.name
                draggable False
                dropped processor.process_drop
                fixed:
                    xysize(1000, 50)
                    $p_color = "#555"
                    if processor.active:
                        $p_color = "#000"
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
                        hbox:
                            xalign 1.0
                            spacing 20
                            style_prefix "radio"
                            textbutton "On":
                                text_color "#000"
                                action Function(turn_on, processor) 
                                selected (processor.active)
                            textbutton "Off":
                                text_color "#000"
                                action Function(turn_off, processor)
                                selected not processor.active