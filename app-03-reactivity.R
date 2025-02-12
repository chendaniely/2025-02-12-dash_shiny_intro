library(shiny)
library(bslib)

# Layout
ui <- bslib::page_fluid(
  # Note that we have to set an `id` and `label` for each widget
  # via the two first positional arguments
  sliderInput("slider_id", "Slider Label", min = 0, max = 5, value = 2),
  br(), # Whitespace
  # Note that the range slider is created with the same function
  # and it detects that it should be a range slider via the `value` parameter
  sliderInput(
    "range_slider_id",
    "A range slider",
    min = 0,
    max = 5,
    value = c(1, 3),
    step = 0.1,
    ticks = FALSE
  ),
  selectInput(
    "city",
    "Select a city",
    choices = c("New York", "Montreal", "San Fransico"),
    selected = "Montreal",
  ),
  br(),
  # selectizeInput allows the use of placeholder text
  # although it's a bit convoluted
  selectizeInput(
    "city_multi",
    "",
    choices = c("New York", "Montreal", "San Fransico"),
    multi = TRUE,
    options = list(
      placeholder = "Select multiple cities",
      onInitialize = I('function() { this.setValue(""); }')
    )
  ),
  textInput("input_widget", ""),
  textOutput("output_area"),
)

# Server side callbacks/reactivity
server <- function(input, output, session) {
  output$output_area <- renderText({
    # Explicit returns are optional in R, but can improve code clarity
    return(input$input_widget)
  })
}

# Run the app/dashboard
shinyApp(ui, server)
