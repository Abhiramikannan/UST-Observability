variable "observe_customer" {
  description = "Observe customer ID"
  type        = string
}

variable "observe_token" {
  description = "Observe API token"
  type        = string
  sensitive   = true          # hides it in terraform output/logs
}

variable "observe_workspace" {
  description = "Observe workspace OID (e.g., o:::workspace:43207155)"
  type        = string
}

variable "observe_raw_dataset" {
  description = "Raw OTEL dataset ID (e.g., 43207633)"
  type        = string
}
