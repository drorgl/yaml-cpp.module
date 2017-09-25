{
    'variables': {
        'library': 'static_library',
        #'library' : 'shared_library',
    },
     'target_defaults': {
		'win_delay_load_hook': 'false',
		'msvs_settings': {
			# This magical incantation is necessary because VC++ will compile
			# object files to same directory... even if they have the same name!
			'VCCLCompilerTool': {
			  'ObjectFile': '$(IntDir)/%(RelativeDir)/',
			  #'AdditionalOptions': [ '/EHsc', '/wd4244']
			  'WarningLevel': 0,
			  'WholeProgramOptimization': 'false',
			  'AdditionalOptions': ['/EHsc'],
			  'ExceptionHandling' : 1, #/EHsc
			},
			
		},
		'configurations':{
			'Debug':{
				'conditions': [
				  ['target_arch=="x64"', {
					'msvs_configuration_platform': 'x64',
				  }],
				  ['1==1',{

					'defines':[
						'DEBUG',
					],
					'msvs_settings': {		
						'VCCLCompilerTool': {
						  #'WholeProgramOptimization' : 'false',
						  #'AdditionalOptions': ['/GL-','/w'], #['/wd4244' ,'/wd4018','/wd4133' ,'/wd4090'] #GL- was added because the forced optimization coming from node-gyp is disturbing the weird coding style from ffmpeg.
						  'WarningLevel': 0,
						  'WholeProgramOptimization': 'false',
						  'AdditionalOptions': ['/EHsc'],
						  'ExceptionHandling' : 1, #/EHsc
						  'RuntimeLibrary': 3, # dll debug
						},
						'VCLinkerTool' : {
							'GenerateDebugInformation' : 'true',
							'conditions':[
								['target_arch=="x64"', {
									'TargetMachine' : 17 # /MACHINE:X64
								}],
							],
							
						}
					}
				
				  }],
				],
				
			},
			'Release':{
				'conditions': [
				  ['target_arch=="x64"', {
					'msvs_configuration_platform': 'x64',
				  }],
				],
				'msvs_settings': {			
					'VCCLCompilerTool': {
						'WholeProgramOptimization' : 'false',
						#'AdditionalOptions': ['/GL-','/w'], #['/wd4244' ,'/wd4018','/wd4133' ,'/wd4090'] #GL- was added because the forced optimization coming from node-gyp is disturbing the weird coding style from ffmpeg.
						'WarningLevel': 0,
						  'WholeProgramOptimization': 'false',
						  'AdditionalOptions': ['/EHsc'],
						  'ExceptionHandling' : 1, #/EHsc
						  'RuntimeLibrary': 2, # dll release
					},
					'VCLinkerTool' : {
						'conditions':[
							['target_arch=="x64"', {
								'TargetMachine' : 17 # /MACHINE:X64
							}],
						],
						
					}
				}
			},
		},
		
		'conditions': [
			['OS == "win"',{
				'defines':[
                    'WIN32',
					'DELAYIMP_INSECURE_WRITABLE_HOOKS'
				],
			}],
		  ['OS != "win"', {
			'defines': [
			  '_LARGEFILE_SOURCE',
			  '_FILE_OFFSET_BITS=64',
			  
			],
			'cflags':[
				'-fPIC',
				'-fexceptions',
			],
			'cflags!': [ '-fno-exceptions' ],
			'cflags_cc!': [ '-fno-exceptions' ],
			'conditions': [
				['OS=="mac"', {
				  'xcode_settings': {
					'GCC_ENABLE_CPP_EXCEPTIONS': 'YES'
				  }
				}]
			],
			'conditions': [
			  ['OS=="solaris"', {
				'cflags': [ '-pthreads' ],
			  }],
			  ['OS not in "solaris android"', {
				'cflags': [ '-pthread' ],
			  }],
			],
		}],
		['OS=="android"',{
			'defines':[
				'ANDROID'
			],
		  }],
		],
	  },

    "targets": [
        {
            'target_name': 'yaml-cpp',
            'type': '<(library)',
            'dependencies': [
            ],
            'include_dirs':[
                "src/include",
                "src/src",
            ],
            "defines":[
            ],
            'direct_dependent_settings': {
                'include_dirs': [
                    "src/include",
                    "src/src",
                ],
                "defines":[
                ],
            },
            'sources':[

                "src/include/yaml-cpp/aliasmanager.h",
                "src/include/yaml-cpp/anchor.h",
                "src/include/yaml-cpp/binary.h",
                "src/include/yaml-cpp/contrib",
                "src/include/yaml-cpp/contrib/anchordict.h",
                "src/include/yaml-cpp/contrib/graphbuilder.h",
                "src/include/yaml-cpp/conversion.h",
                "src/include/yaml-cpp/dll.h",
                "src/include/yaml-cpp/emitfromevents.h",
                "src/include/yaml-cpp/emitter.h",
                "src/include/yaml-cpp/emittermanip.h",
                "src/include/yaml-cpp/eventhandler.h",
                "src/include/yaml-cpp/exceptions.h",
                "src/include/yaml-cpp/iterator.h",
                "src/include/yaml-cpp/ltnode.h",
                "src/include/yaml-cpp/mark.h",
                "src/include/yaml-cpp/node.h",
                "src/include/yaml-cpp/nodeimpl.h",
                "src/include/yaml-cpp/nodereadimpl.h",
                "src/include/yaml-cpp/nodeutil.h",
                "src/include/yaml-cpp/noncopyable.h",
                "src/include/yaml-cpp/null.h",
                "src/include/yaml-cpp/ostream.h",
                "src/include/yaml-cpp/parser.h",
                "src/include/yaml-cpp/stlemitter.h",
                "src/include/yaml-cpp/stlnode.h",
                "src/include/yaml-cpp/traits.h",
                "src/include/yaml-cpp/yaml.h",
                
                
                #"src/LICENSE",
                #"src/README.md",
                
                "src/src/aliasmanager.cpp",
                "src/src/binary.cpp",
                "src/src/collectionstack.h",
                "src/src/contrib",
                "src/src/contrib/graphbuilder.cpp",
                "src/src/contrib/graphbuilderadapter.cpp",
                "src/src/contrib/graphbuilderadapter.h",
                "src/src/conversion.cpp",
                "src/src/directives.cpp",
                "src/src/directives.h",
                "src/src/emitfromevents.cpp",
                "src/src/emitter.cpp",
                "src/src/emitterstate.cpp",
                "src/src/emitterstate.h",
                "src/src/emitterutils.cpp",
                "src/src/emitterutils.h",
                "src/src/exp.cpp",
                "src/src/exp.h",
                "src/src/indentation.h",
                "src/src/iterator.cpp",
                "src/src/iterpriv.h",
                "src/src/node.cpp",
                "src/src/nodebuilder.cpp",
                "src/src/nodebuilder.h",
                "src/src/nodeownership.cpp",
                "src/src/nodeownership.h",
                "src/src/null.cpp",
                "src/src/ostream.cpp",
                "src/src/parser.cpp",
                "src/src/ptr_stack.h",
                "src/src/ptr_vector.h",
                "src/src/regex.cpp",
                "src/src/regex.h",
                "src/src/regeximpl.h",
                "src/src/scanner.cpp",
                "src/src/scanner.h",
                "src/src/scanscalar.cpp",
                "src/src/scanscalar.h",
                "src/src/scantag.cpp",
                "src/src/scantag.h",
                "src/src/scantoken.cpp",
                "src/src/setting.h",
                "src/src/simplekey.cpp",
                "src/src/singledocparser.cpp",
                "src/src/singledocparser.h",
                "src/src/stream.cpp",
                "src/src/stream.h",
                "src/src/streamcharsource.h",
                "src/src/stringsource.h",
                "src/src/tag.cpp",
                "src/src/tag.h",
                "src/src/token.h",
            ]
        },
        {
            'target_name': 'yaml-cpp-test',
            'type': 'executable',
            'dependencies': [
                'yaml-cpp'
            ],
            'include_dirs':[
                "src/test/",
                "src/include",
                "src/test/gtest-1.8.0/googlemock",
                "src/test/gtest-1.8.0/googlemock/include",
                "src/test/gtest-1.8.0/googletest",
                "src/test/gtest-1.8.0/googletest/include",
            ],
            "defines":[
            ],
            'direct_dependent_settings': {
                'include_dirs': [
                    "src/test/",
                    "src/include",
                    "src/test/gtest-1.8.0/googlemock",
                    "src/test/gtest-1.8.0/googlemock/include",
                    "src/test/gtest-1.8.0/googletest",
                    "src/test/gtest-1.8.0/googletest/include",
                ],
                "defines":[
                ],
            },
            'sources':[
                "src/test/emittertests.cpp",
                "src/test/emittertests.h",
                "src/test/main.cpp",
                "src/test/nodetests.h",
                "src/test/old-api/parsertests.cpp",
                "src/test/old-api/spectests.cpp",
                "src/test/parsertests.h",
                "src/test/specexamples.h",
                "src/test/spectests.cpp",
                "src/test/spectests.h",
                "src/test/tests.cpp",
                "src/test/tests.h",

                #"src/test/gtest-1.8.0/googlemock/include/gmock/gmock.h",
                #"src/test/gtest-1.8.0/googlemock/include/gmock/internal/custom/gmock-generated-actions.h",
                #"src/test/gtest-1.8.0/googlemock/include/gmock/internal/custom/gmock-generated-actions.h.pump",
                #"src/test/gtest-1.8.0/googlemock/include/gmock/internal/custom/gmock-matchers.h",
                #"src/test/gtest-1.8.0/googlemock/include/gmock/internal/custom/gmock-port.h",
                #"src/test/gtest-1.8.0/googlemock/include/gmock/internal/gmock-generated-internal-utils.h",
                #"src/test/gtest-1.8.0/googlemock/include/gmock/internal/gmock-generated-internal-utils.h.pump",
                #"src/test/gtest-1.8.0/googlemock/include/gmock/internal/gmock-internal-utils.h",
                #"src/test/gtest-1.8.0/googlemock/include/gmock/internal/gmock-port.h",
                #"src/test/gtest-1.8.0/googlemock/src/gmock-all.cc",
                ##"src/test/gtest-1.8.0/googlemock/src/gmock-cardinalities.cc",
                ##"src/test/gtest-1.8.0/googlemock/src/gmock-internal-utils.cc",
                ##"src/test/gtest-1.8.0/googlemock/src/gmock-matchers.cc",
                ##"src/test/gtest-1.8.0/googlemock/src/gmock-spec-builders.cc",
                ##"src/test/gtest-1.8.0/googlemock/src/gmock.cc",
                ##"src/test/gtest-1.8.0/googlemock/src/gmock_main.cc",
#
                #"src/test/gtest-1.8.0/googletest/include/gtest/gtest.h",
                #"src/test/gtest-1.8.0/googletest/src/gtest-all.cc",
                ##"src/test/gtest-1.8.0/googletest/src/gtest-death-test.cc",
                ##"src/test/gtest-1.8.0/googletest/src/gtest-filepath.cc",
                ##"src/test/gtest-1.8.0/googletest/src/gtest-internal-inl.h",
                ##"src/test/gtest-1.8.0/googletest/src/gtest-port.cc",
                ##"src/test/gtest-1.8.0/googletest/src/gtest-printers.cc",
                ##"src/test/gtest-1.8.0/googletest/src/gtest-test-part.cc",
                ##"src/test/gtest-1.8.0/googletest/src/gtest-typed-test.cc",
                ##"src/test/gtest-1.8.0/googletest/src/gtest.cc",
                ##"src/test/gtest-1.8.0/googletest/src/gtest_main.cc",
#
                ##"src/test/gtest-1.8.0/googlemock/include/gmock/gmock-actions.h",
                ##"src/test/gtest-1.8.0/googlemock/include/gmock/gmock-cardinalities.h",
                ##"src/test/gtest-1.8.0/googlemock/include/gmock/gmock-generated-actions.h",
                ##"src/test/gtest-1.8.0/googlemock/include/gmock/gmock-generated-actions.h.pump",
                ##"src/test/gtest-1.8.0/googlemock/include/gmock/gmock-generated-function-mockers.h",
                ##"src/test/gtest-1.8.0/googlemock/include/gmock/gmock-generated-function-mockers.h.pump",
                ##"src/test/gtest-1.8.0/googlemock/include/gmock/gmock-generated-matchers.h",
                ##"src/test/gtest-1.8.0/googlemock/include/gmock/gmock-generated-matchers.h.pump",
                ##"src/test/gtest-1.8.0/googlemock/include/gmock/gmock-generated-nice-strict.h",
                ##"src/test/gtest-1.8.0/googlemock/include/gmock/gmock-generated-nice-strict.h.pump",
                ##"src/test/gtest-1.8.0/googlemock/include/gmock/gmock-matchers.h",
                ##"src/test/gtest-1.8.0/googlemock/include/gmock/gmock-more-actions.h",
                ##"src/test/gtest-1.8.0/googlemock/include/gmock/gmock-more-matchers.h",
                ##"src/test/gtest-1.8.0/googlemock/include/gmock/gmock-spec-builders.h",
                #
#
                ##"src/test/gtest-1.8.0/googlemock/test/gmock-actions_test.cc",
                ##"src/test/gtest-1.8.0/googlemock/test/gmock-cardinalities_test.cc",
                ##"src/test/gtest-1.8.0/googlemock/test/gmock-generated-actions_test.cc",
                ##"src/test/gtest-1.8.0/googlemock/test/gmock-generated-function-mockers_test.cc",
                ##"src/test/gtest-1.8.0/googlemock/test/gmock-generated-internal-utils_test.cc",
                ##"src/test/gtest-1.8.0/googlemock/test/gmock-generated-matchers_test.cc",
                ##"src/test/gtest-1.8.0/googlemock/test/gmock-internal-utils_test.cc",
                ##"src/test/gtest-1.8.0/googlemock/test/gmock-matchers_test.cc",
                ##"src/test/gtest-1.8.0/googlemock/test/gmock-more-actions_test.cc",
                ##"src/test/gtest-1.8.0/googlemock/test/gmock-nice-strict_test.cc",
                ##"src/test/gtest-1.8.0/googlemock/test/gmock-port_test.cc",
                ##"src/test/gtest-1.8.0/googlemock/test/gmock-spec-builders_test.cc",
                ##"src/test/gtest-1.8.0/googlemock/test/gmock_all_test.cc",
                ##"src/test/gtest-1.8.0/googlemock/test/gmock_ex_test.cc",
                ##"src/test/gtest-1.8.0/googlemock/test/gmock_leak_test_.cc",
                ##"src/test/gtest-1.8.0/googlemock/test/gmock_link2_test.cc",
                ##"src/test/gtest-1.8.0/googlemock/test/gmock_link_test.cc",
                ##"src/test/gtest-1.8.0/googlemock/test/gmock_link_test.h",
                ##"src/test/gtest-1.8.0/googlemock/test/gmock_output_test_.cc",
                ##"src/test/gtest-1.8.0/googlemock/test/gmock_output_test_golden.txt",
                ##"src/test/gtest-1.8.0/googlemock/test/gmock_stress_test.cc",
                ##"src/test/gtest-1.8.0/googlemock/test/gmock_test.cc",
                ##"src/test/gtest-1.8.0/googletest/codegear/gtest_all.cc",
                ##"src/test/gtest-1.8.0/googletest/codegear/gtest_link.cc",
                ##"src/test/gtest-1.8.0/googletest/include/gtest/gtest-death-test.h",
                ##"src/test/gtest-1.8.0/googletest/include/gtest/gtest-message.h",
                ##"src/test/gtest-1.8.0/googletest/include/gtest/gtest-param-test.h",
                ##"src/test/gtest-1.8.0/googletest/include/gtest/gtest-param-test.h.pump",
                ##"src/test/gtest-1.8.0/googletest/include/gtest/gtest-printers.h",
                ##"src/test/gtest-1.8.0/googletest/include/gtest/gtest-spi.h",
                ##"src/test/gtest-1.8.0/googletest/include/gtest/gtest-test-part.h",
                ##"src/test/gtest-1.8.0/googletest/include/gtest/gtest-typed-test.h",
                #
                ##"src/test/gtest-1.8.0/googletest/include/gtest/gtest_pred_impl.h",
                ##"src/test/gtest-1.8.0/googletest/include/gtest/gtest_prod.h",
                ##"src/test/gtest-1.8.0/googletest/include/gtest/internal/custom/gtest-port.h",
                ##"src/test/gtest-1.8.0/googletest/include/gtest/internal/custom/gtest-printers.h",
                ##"src/test/gtest-1.8.0/googletest/include/gtest/internal/custom/gtest.h",
                ##"src/test/gtest-1.8.0/googletest/include/gtest/internal/gtest-death-test-internal.h",
                ##"src/test/gtest-1.8.0/googletest/include/gtest/internal/gtest-filepath.h",
                ##"src/test/gtest-1.8.0/googletest/include/gtest/internal/gtest-internal.h",
                ##"src/test/gtest-1.8.0/googletest/include/gtest/internal/gtest-linked_ptr.h",
                ##"src/test/gtest-1.8.0/googletest/include/gtest/internal/gtest-param-util-generated.h",
                ##"src/test/gtest-1.8.0/googletest/include/gtest/internal/gtest-param-util-generated.h.pump",
                ##"src/test/gtest-1.8.0/googletest/include/gtest/internal/gtest-param-util.h",
                ##"src/test/gtest-1.8.0/googletest/include/gtest/internal/gtest-port-arch.h",
                ##"src/test/gtest-1.8.0/googletest/include/gtest/internal/gtest-port.h",
                ##"src/test/gtest-1.8.0/googletest/include/gtest/internal/gtest-string.h",
                ##"src/test/gtest-1.8.0/googletest/include/gtest/internal/gtest-tuple.h",
                ##"src/test/gtest-1.8.0/googletest/include/gtest/internal/gtest-tuple.h.pump",
                ##"src/test/gtest-1.8.0/googletest/include/gtest/internal/gtest-type-util.h",
                ##"src/test/gtest-1.8.0/googletest/include/gtest/internal/gtest-type-util.h.pump",
                ##"src/test/gtest-1.8.0/googletest/LICENSE",
                ##"src/test/gtest-1.8.0/googletest/samples/prime_tables.h",
                ##"src/test/gtest-1.8.0/googletest/samples/sample1.cc",
                ##"src/test/gtest-1.8.0/googletest/samples/sample1.h",
                ##"src/test/gtest-1.8.0/googletest/samples/sample10_unittest.cc",
                ##"src/test/gtest-1.8.0/googletest/samples/sample1_unittest.cc",
                ##"src/test/gtest-1.8.0/googletest/samples/sample2.cc",
                ##"src/test/gtest-1.8.0/googletest/samples/sample2.h",
                ##"src/test/gtest-1.8.0/googletest/samples/sample2_unittest.cc",
                ##"src/test/gtest-1.8.0/googletest/samples/sample3-inl.h",
                ##"src/test/gtest-1.8.0/googletest/samples/sample3_unittest.cc",
                ##"src/test/gtest-1.8.0/googletest/samples/sample4.cc",
                ##"src/test/gtest-1.8.0/googletest/samples/sample4.h",
                ##"src/test/gtest-1.8.0/googletest/samples/sample4_unittest.cc",
                ##"src/test/gtest-1.8.0/googletest/samples/sample5_unittest.cc",
                ##"src/test/gtest-1.8.0/googletest/samples/sample6_unittest.cc",
                ##"src/test/gtest-1.8.0/googletest/samples/sample7_unittest.cc",
                ##"src/test/gtest-1.8.0/googletest/samples/sample8_unittest.cc",
                ##"src/test/gtest-1.8.0/googletest/samples/sample9_unittest.cc",
               #
                ##"src/test/gtest-1.8.0/googletest/test/gtest-death-test_ex_test.cc",
                ##"src/test/gtest-1.8.0/googletest/test/gtest-death-test_test.cc",
                ##"src/test/gtest-1.8.0/googletest/test/gtest-filepath_test.cc",
                ##"src/test/gtest-1.8.0/googletest/test/gtest-linked_ptr_test.cc",
                ##"src/test/gtest-1.8.0/googletest/test/gtest-listener_test.cc",
                ##"src/test/gtest-1.8.0/googletest/test/gtest-message_test.cc",
                ##"src/test/gtest-1.8.0/googletest/test/gtest-options_test.cc",
                ##"src/test/gtest-1.8.0/googletest/test/gtest-param-test2_test.cc",
                ##"src/test/gtest-1.8.0/googletest/test/gtest-param-test_test.cc",
                ##"src/test/gtest-1.8.0/googletest/test/gtest-param-test_test.h",
                ##"src/test/gtest-1.8.0/googletest/test/gtest-port_test.cc",
                ##"src/test/gtest-1.8.0/googletest/test/gtest-printers_test.cc",
                ##"src/test/gtest-1.8.0/googletest/test/gtest-test-part_test.cc",
                ##"src/test/gtest-1.8.0/googletest/test/gtest-tuple_test.cc",
                ##"src/test/gtest-1.8.0/googletest/test/gtest-typed-test2_test.cc",
                ##"src/test/gtest-1.8.0/googletest/test/gtest-typed-test_test.cc",
                ##"src/test/gtest-1.8.0/googletest/test/gtest-typed-test_test.h",
                ##"src/test/gtest-1.8.0/googletest/test/gtest-unittest-api_test.cc",
                ##"src/test/gtest-1.8.0/googletest/test/gtest_all_test.cc",
                ##"src/test/gtest-1.8.0/googletest/test/gtest_break_on_failure_unittest.py",
                ##"src/test/gtest-1.8.0/googletest/test/gtest_break_on_failure_unittest_.cc",
                ##"src/test/gtest-1.8.0/googletest/test/gtest_catch_exceptions_test.py",
                ##"src/test/gtest-1.8.0/googletest/test/gtest_catch_exceptions_test_.cc",
                ##"src/test/gtest-1.8.0/googletest/test/gtest_color_test.py",
                ##"src/test/gtest-1.8.0/googletest/test/gtest_color_test_.cc",
                ##"src/test/gtest-1.8.0/googletest/test/gtest_environment_test.cc",
                ##"src/test/gtest-1.8.0/googletest/test/gtest_env_var_test.py",
                ##"src/test/gtest-1.8.0/googletest/test/gtest_env_var_test_.cc",
                ##"src/test/gtest-1.8.0/googletest/test/gtest_filter_unittest.py",
                ##"src/test/gtest-1.8.0/googletest/test/gtest_filter_unittest_.cc",
                ##"src/test/gtest-1.8.0/googletest/test/gtest_help_test.py",
                ##"src/test/gtest-1.8.0/googletest/test/gtest_help_test_.cc",
                ##"src/test/gtest-1.8.0/googletest/test/gtest_list_tests_unittest.py",
                ##"src/test/gtest-1.8.0/googletest/test/gtest_list_tests_unittest_.cc",
                ##"src/test/gtest-1.8.0/googletest/test/gtest_main_unittest.cc",
                ##"src/test/gtest-1.8.0/googletest/test/gtest_no_test_unittest.cc",
                ##"src/test/gtest-1.8.0/googletest/test/gtest_output_test.py",
                ##"src/test/gtest-1.8.0/googletest/test/gtest_output_test_.cc",
                ##"src/test/gtest-1.8.0/googletest/test/gtest_output_test_golden_lin.txt",
                ##"src/test/gtest-1.8.0/googletest/test/gtest_pred_impl_unittest.cc",
                ##"src/test/gtest-1.8.0/googletest/test/gtest_premature_exit_test.cc",
                ##"src/test/gtest-1.8.0/googletest/test/gtest_prod_test.cc",
                ##"src/test/gtest-1.8.0/googletest/test/gtest_repeat_test.cc",
                ##"src/test/gtest-1.8.0/googletest/test/gtest_shuffle_test.py",
                ##"src/test/gtest-1.8.0/googletest/test/gtest_shuffle_test_.cc",
                ##"src/test/gtest-1.8.0/googletest/test/gtest_sole_header_test.cc",
                ##"src/test/gtest-1.8.0/googletest/test/gtest_stress_test.cc",
                ##"src/test/gtest-1.8.0/googletest/test/gtest_test_utils.py",
                ##"src/test/gtest-1.8.0/googletest/test/gtest_throw_on_failure_ex_test.cc",
                ##"src/test/gtest-1.8.0/googletest/test/gtest_throw_on_failure_test.py",
                ##"src/test/gtest-1.8.0/googletest/test/gtest_throw_on_failure_test_.cc",
                ##"src/test/gtest-1.8.0/googletest/test/gtest_uninitialized_test.py",
                ##"src/test/gtest-1.8.0/googletest/test/gtest_uninitialized_test_.cc",
                ##"src/test/gtest-1.8.0/googletest/test/gtest_unittest.cc",
                ##"src/test/gtest-1.8.0/googletest/test/gtest_xml_outfile1_test_.cc",
                ##"src/test/gtest-1.8.0/googletest/test/gtest_xml_outfile2_test_.cc",
                ##"src/test/gtest-1.8.0/googletest/test/gtest_xml_output_unittest_.cc",
                ##"src/test/gtest-1.8.0/googletest/test/production.cc",
                ##"src/test/gtest-1.8.0/googletest/test/production.h",
                ##"src/test/gtest-1.8.0/googletest/xcode/Samples/FrameworkSample/widget.cc",
                ##"src/test/gtest-1.8.0/googletest/xcode/Samples/FrameworkSample/widget.h",
                ##"src/test/gtest-1.8.0/googletest/xcode/Samples/FrameworkSample/widget_test.cc",
             #
                ##"src/util/api.cpp",
                ##"src/util/parse.cpp",
                ##"src/util/read.cpp",
                ##"src/util/sandbox.cpp",
                ##"yaml-cpp.gyp",
                ##"build_windows.bat",
                ##"src/CONTRIBUTING.md",

            ]
        }
    ]
}
