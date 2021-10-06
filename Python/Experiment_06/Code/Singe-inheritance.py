class Country:
    def ShowCountry(self):
        print("This is India");

# inheritance
class State(Country):
    def ShowState(self):
        print("This is State");

st = State();

st.ShowCountry();

st.ShowState();
