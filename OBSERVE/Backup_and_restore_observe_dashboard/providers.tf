terraform {
  required_providers {
    observe = {
      source  = "observeinc/observe"
      version = "~> 0.14"
    }
  }
}

provider "observe" {
  customer  = "109714025826"
  domain    = "observeinc.com"
  api_token = var.observe_token
}
