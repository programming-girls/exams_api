import sentry_sdk
sentry_sdk.init(
    "https://797518561ab64df9a5f8eef85be584c2@o1085653.ingest.sentry.io/6096701",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)