# If you want the same port each time and enable hot reloading
# options(shiny.port = 8050, shiny.autoreload = TRUE)

library(shiny)
library(bslib)


# Layout
ui <- bslib::page_fluid("I am alive")

# Server side callbacks/reactivity
server <- function(input, output, session) {}

# Run the app/dashboard
shinyApp(ui, server)
