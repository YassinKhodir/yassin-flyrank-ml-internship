# The one interactive feature: CTR calculator
AI-assisted study draft. The student has not claimed to write this unaided.

A backend is the part of an application that runs on a server. It might store
a message or read a database. This feature does not need an application backend.
It only calculates numbers entered in the browser. The hosting service delivers
the files; JavaScript in the visitor's browser does the calculation.

The visitor enters clicks and impressions, then presses Calculate CTR.
CTR means click-through rate. The form hands the entered values to JavaScript.
The code checks that both values exist, are whole numbers, are non-negative,
and are within JavaScript's safe integer range. If impressions are zero, it
explains that CTR cannot be calculated. Otherwise it divides clicks by
impressions, multiplies by 100, and prints the calculation and percentage.
It rounds the displayed percentage to at most four decimal places.

Data flow: form fields → local checks → arithmetic → visible result.
The calculator sends no request, stores no record, and emails nobody.
Reloading the page resets it. It does not call Ollama, Gemma or any AI service.
It is an arithmetic demo related to the internship, not a browser version of
the complete Python study coach.

Ten clicks and 100 impressions produce 10%. Zero impressions produce a clear
message. Negative values, fractions and unsafe values are rejected. Counts
represent events, not different people. The result alone does not show whether
performance is good. A comparison or target is needed. The calculator does
not assume clicks must be below impressions for every possible tracking setup;
the visitor must check that the two counts refer to compatible events and periods.

The dynamic-feature assignment also asks the student to understand and explain
the data flow. This document supports that learning but does not prove it happened.
