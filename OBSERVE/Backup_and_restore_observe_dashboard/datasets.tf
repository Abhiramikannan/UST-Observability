resource "observe_dataset" "otel_logs" {
    acceleration_disabled = false
    freshness             = "2m0s"
    
    inputs = {
        (var.observe_raw_dataset) = "o:::dataset:${var.observe_raw_dataset}"
    }
    
    name      = "Otel logs"
    workspace =  var.observe_workspace

    stage {
        output_stage = false
        pipeline     = <<-EOT
            filter OBSERVATION_KIND = "otellogs"
            make_col timestamp:BUNDLE_TIMESTAMP
            make_col body:string(FIELDS.logs.body)
            make_col severity:string(FIELDS.logs.severity_text)
            make_col service_name:string(FIELDS.resource.attributes."service.name")
            make_col host_name:string(FIELDS.resource.attributes."host.name")
            set_valid_from options(max_time_diff:4h), timestamp
            interface "log", log:body
        EOT
    }
}

resource "observe_dataset" "otel_metrics" {
    acceleration_disabled = false
    freshness             = "2m0s"
    
    inputs = {
        "OTEL Connector_${var.observe_raw_dataset}" = "o:::dataset:${var.observe_raw_dataset}"
    }

    
    name      = "Otel metrics"
    workspace = var.observe_workspace

    stage {
        output_stage = false
        pipeline     = <<-EOT
            filter OBSERVATION_KIND = "otelmetrics"
            make_col metric:string(FIELDS.name)
            make_col value:float64(FIELDS.value)
            make_col timestamp:BUNDLE_TIMESTAMP
            make_col service_name:string(EXTRA.resource.attributes."service.name")
            make_col host_name:string(EXTRA.resource.attributes."host.name")
            set_valid_from options(max_time_diff:4h), timestamp
            interface "metric", metric: metric, value:value
        EOT
    }
}

output "otel_metrics_id" {
    value = observe_dataset.otel_metrics.id
}

output "otel_logs_id" {
    value = observe_dataset.otel_logs.id
}
