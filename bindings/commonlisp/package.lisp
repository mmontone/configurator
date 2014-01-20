(defpackage configurator
  (:nicknames :config)
  (:use :cl)
  (:export #:configurator-get
	   #:configurator-set
	   #:configurator-setup
	   #:configurator-setup-example
	   #:configurator-list-configs
	   #:configurator-inspect
	   #:configurator-get*
	   #:parse-configuration-option
	   #:with-configuration
	   #:config-get
	   #:config-set
	   #:in-configuration
	   #:get-current-configuration))